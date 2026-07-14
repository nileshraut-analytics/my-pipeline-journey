from pyspark.sql import SparkSession
from pyspark.sql import functions as F
import logging
from datetime import datetime
from time import time
from config import DB_HOST, DB_NAME, DB_PASSWORD, DB_USER
from functools import reduce

logging.basicConfig(
    filename="pipeline.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

spark = SparkSession.builder \
    .appName("Mini Pipeline") \
    .config("spark.jars", "file:///C:/hadoop/bin/postgresql-42.7.3.jar") \
    .getOrCreate()

def load_data():
    try:
        df = spark.read.jdbc(
            url=f"jdbc:postgresql://{DB_HOST}/{DB_NAME}",
            table="amazon_sales",
            properties={
                "user" : DB_USER,
                "password" : DB_PASSWORD,
                "driver" : "org.postgresql.Driver"
            }
        )
        print(f"{get_timestamp()} [LOAD] Loaded {df.count()} rows from PostgreSQL\n")
        logging.info(f"[LOAD] loaded {df.count()} rows from PostgreSQL")
        return df
    except Exception as e:
        print(f"{get_timestamp()} [LOAD] Failed to load data. Error : {e}")
        logging.error(f"[LOAD] Failed to load data. Error: {e}")
        return None
    
def validate_data(df):
    df = df.withColumn("amount", F.expr("try_cast(amount as double)"))
    df = df.withColumn("product", F.lower(F.trim(df["product"])))
    df = df.replace(["None", "NULL", "null", "N/A", ""], None)
    bad_condition = reduce(lambda a, b:a | b, [F.col(c).isNull() for c in df.columns])
    bad_rows = df.filter(bad_condition)
    clean_rows = df.filter(~bad_condition)
    clean_rows = clean_rows.cache()
    clean_rows_count = clean_rows.count()
    bad_rows = bad_rows.cache()
    bad_rows_count = bad_rows.count()
    print(f"{get_timestamp()} [VALIDATE]  found {bad_rows_count} bad rows")
    logging.info(f"[VALIDATE]  found {bad_rows_count} bad rows")
    print(f"{get_timestamp()} [VALIDATE]  found {clean_rows_count} clean rows\n")
    logging.info(f"[VALIDATE]  found {clean_rows_count} clean rows")
    return clean_rows, bad_rows, clean_rows_count, bad_rows_count

def aggregate_data(clean_rows, clean_rows_count):
    final_df = clean_rows.groupBy("product").agg(
        F.count("product").alias("product_count"),
        F.sum("amount").alias("total_sales"),
        F.max("amount").alias("max_amount"),
        F.min("amount").alias("min_amount"),
        F.avg("amount").alias("avg_amount")
    )
    final_df.cache()
    final_df_count = final_df.count()
    print(f"{get_timestamp()} [AGGREGATE] Aggregated {final_df_count} products from {clean_rows_count} rows\n")
    logging.info(f"[AGGREGATE] Aggregated {final_df_count} products from {clean_rows_count} rows")
    
    return final_df, final_df_count

def data_quality_report(df, clean_rows_count, bad_rows_count, final_df_count):
    report = {
        "total_rows" : df.count(),
        "clean_rows" : clean_rows_count,
        "bad_rows" : bad_rows_count,
        "unique_products" : final_df_count
    }

    report_df = spark.createDataFrame([report])
    report_df.toPandas().to_csv("data_quality_report.csv", index=False)
    print(f"{get_timestamp()} [REPORT] Saved data_quality_report.csv\n")
    logging.info(f"[REPORT] Saved data_quality_report.csv")
    return report_df

def run_pipeline():
    start_time = time()
    df = load_data()
    
    if df is None:
        return
    clean_rows, bad_rows, clean_rows_count, bad_rows_count = validate_data(df)
    
    final_df, final_df_count = aggregate_data(clean_rows, clean_rows_count)
    final_df.toPandas().to_csv("output.csv", index=False)
    try:
        final_df.write.jdbc(
            url=f"jdbc:postgresql://{DB_HOST}/{DB_NAME}",
            table="aggregated_sales",
            mode="overwrite",
            properties={
                "user" : DB_USER,
                "password" : DB_PASSWORD,
                "driver" : "org.postgresql.Driver"
            }
        )
        print(f"{get_timestamp()} [DB] Loaded {final_df_count} rows into aggregated_sales\n")
        logging.info(f"[DB] Loaded {final_df_count} rows into aggregated_sales")
    except Exception as e:
        print(f"{get_timestamp()} [DB] Failed to write to PostgreSQL. Error: {e}")
        logging.error(f"[DB] Failed to write to PostgreSQL. Error: {e}")
    
    clean_rows.toPandas().to_csv("clean_data.csv", index=False)
    bad_rows.toPandas().to_csv("bad_data.csv", index=False)

    data_quality_report(df, clean_rows_count, bad_rows_count, final_df_count)

    end_time = time()
    execution_time = end_time - start_time

    print(f"[OUTPUT] clean_data.csv : {clean_rows_count} rows")
    print(f"[OUTPUT] bad_rows.csv : {bad_rows_count} rows\n")
    print(f"{get_timestamp()} [PIPELINE] Completed successfully!")
    logging.info(f"[PIPELINE] Completed successfully!")
    print(f"{get_timestamp()} [PIPELINE] Total execution time: {execution_time:.2f} seconds")
    logging.info(f"[PIPELINE] Total execution time: {execution_time:.2f} seconds")
    clean_rows.unpersist()
    bad_rows.unpersist()
    final_df.unpersist()

if __name__ == "__main__":
    run_pipeline()
