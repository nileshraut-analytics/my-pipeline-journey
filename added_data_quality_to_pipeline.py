import psycopg2
import pandas as pd
import logging
from config import DB_HOST, DB_NAME, DB_PASSWORD, DB_USER
from datetime import datetime
from sqlalchemy import create_engine
from time import time

logging.basicConfig(
    filename="pipeline.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

def data_quality_report(df, bad_rows, clean_rows, final_df):
    report_df = pd.DataFrame({
        "metric" : ["total_rows", "bad_rows", "clean_rows", "unique_products"],
        "value" : [len(df), len(bad_rows), len(clean_rows), len(final_df)]
    })
    report_df.to_csv("data_quality_report.csv", index=False)
    print(f"[REPORT] Saved data_quality_report.csv\n")
    logging.info(f"[REPORT] Saved data_quality_report.csv")
    return report_df

def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def load_data():
    try:
        conn = psycopg2.connect(
        host = DB_HOST,
        database = DB_NAME,
        user = DB_USER,
        password = DB_PASSWORD
    )
        
        query = "SELECT * FROM amazon_sales"
        df = pd.read_sql(query, conn)
        print(f"{get_timestamp()} [LOAD]  Loaded {len(df)} rows from PostgreSQL\n")
        logging.info(f"[LOAD]  Loaded {len(df)} rows from PostgreSQL")
        return df
    except Exception as e:
        print(f"[LOAD]  failed to load data from PostgreSQL")
        print(f"Error : {e}")
        
def validate_data(df):
    df["amount"] = pd.to_numeric(df["amount"],errors="coerce")
    df["product"] = df["product"].str.strip().str.lower()
    bad_rows = df[df.isnull().any(axis = 1)].copy()
    clean_rows = df.dropna().copy()
    print(f"{get_timestamp()} [VALIDATE]  found {len(bad_rows)} bad rows")
    logging.info(f"[VALIDATE]  found {len(bad_rows)} bad rows")
    print(f"{get_timestamp()} [VALIDATE]  found {len(clean_rows)} clean rows\n")
    logging.info(f"[VALIDATE]  found {len(clean_rows)} clean rows")
    return bad_rows, clean_rows

def aggregate_data(clean_rows):
    final_df = clean_rows.groupby("product")["amount"].agg(
        count = "count",
        total = "sum",
        max = "max",
        min = "min"
    ).reset_index()
    print(f"{get_timestamp()} [AGGREGATE] Aggregated {len(final_df)} products from {len(clean_rows)} rows\n")
    logging.info(f"[AGGREGATE] Aggregated {len(final_df)} products from {len(clean_rows)} rows")
    return final_df

def clean_output(final_df):
    print(f"{get_timestamp()} [OUTPUT] Saved aggregated data to new_output.csv\n")
    logging.info(f"[OUTPUT] Saved aggregated data to new_output.csv")
    final_df.to_csv("new_output.csv", index=False)

    try:
        engine = create_engine(f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}")
        final_df.to_sql(
            "aggregated_sales",
            engine,
            if_exists = "replace",
            index = False
        )
        print(f"{get_timestamp()} [DB] Loaded {len(final_df)} rows into aggregated_sales\n")
        logging.info(f"[DB] Loaded {len(final_df)} rows into aggregated_sales")
    except Exception as e:
        print(f"{get_timestamp()} [DB] Failed to load aggregated data.")
        print(f"Error: {e}")
    
def errors_log(bad_rows):
    print(f"{get_timestamp()} [OUTPUT] Saved bad rows to errors_log.csv\n")
    logging.info(f"[OUTPUT] Saved bad rows to errors_log.csv")
    return bad_rows.to_csv("errors_log.csv", index=False)

def run_pipeline():
    start_time = time()
    df = load_data()

    if df is None:
        return
    
    bad_rows, clean_rows = validate_data(df)
    final_df = aggregate_data(clean_rows)
    clean_output(final_df)
    errors_log(bad_rows)
    report_df = data_quality_report(df, bad_rows, clean_rows, final_df)
    end_time = time()
    execution_time = end_time - start_time
    print(f"{get_timestamp()} [PIPELINE] Completed successfully!")
    logging.info(f"[PIPELINE] Completed successfully!")
    print(f"{get_timestamp()} [PIPELINE] Total execution time: {execution_time:.2f} seconds")
    logging.info(f"[PIPELINE] Total execution time: {execution_time:.2f} seconds")

run_pipeline()