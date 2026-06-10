import psycopg2
import pandas as pd
from config import DB_HOST, DB_NAME, DB_USER, DB_PASSWORD
from datetime import datetime
from sqlalchemy import create_engine

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
        print(f"{get_timestamp()} [LOAD]  Loaded {len(df)} rows from postgreSQL\n")
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
    print(f"{get_timestamp()} [VALIDATE]  found {len(clean_rows)} clean rows\n")
    return bad_rows, clean_rows

def aggregate_data(clean_rows):
    final_df = clean_rows.groupby("product")["amount"].agg(
        count = "count",
        total = "sum",
        max = "max",
        min = "min"
    ).reset_index()
    print(f"{get_timestamp()} [AGGREGATE] Aggregated {len(final_df)} products from {len(clean_rows)} rows\n")
    return final_df

def clean_output(final_df):
    print(f"{get_timestamp()} [OUTPUT] Saved aggregated data to new_output.csv\n")
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
    except Exception as e:
        print(f"{get_timestamp()} [DB] Failed to load aggregated data.")
        print(f"Error: {e}")
    
def errors_log(bad_rows):
    print(f"{get_timestamp()} [OUTPUT] Saved bad rows to errors_log.csv\n")
    return bad_rows.to_csv("errors_log.csv", index=False)

def run_pipeline():
    df = load_data()

    if df is None:
        return
    
    bad_rows, clean_rows = validate_data(df)
    final_df = aggregate_data(clean_rows)
    clean_output(final_df)
    errors_log(bad_rows)
    print(f"{get_timestamp()} [PIPELINE] Completed successfully!")

run_pipeline()
