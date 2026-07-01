from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = SparkSession.builder.appName("Mini Pipeline").getOrCreate()

def load_data():
    try:
        df = spark.read.csv("sales_input.csv", header=True)
        print(f"[LOAD] Loaded {df.count()} rows from CSV")
        return df
    except Exception as e:
        print(f"[LOAD] Failed to load data")
        print(f"Error: {e}")
        return None
    
def validate_data(df):
    df = df.withColumn("amount", F.expr("try_cast(amount as double)"))
    df = df.withColumn("product", F.lower(F.trim(df["product"])))
    clean_rows = df.na.drop()
    bad_rows = df.subtract(clean_rows)
    return clean_rows, bad_rows

def aggregate_data(clean_rows):
    final_df = clean_rows.groupBy("product").agg(
        F.count("product").alias("product_count"),
        F.sum("amount").alias("total_sales"),
        F.max("amount").alias("max_amount"),
        F.min("amount").alias("min_amount"),
        F.avg("amount").alias("avg_amount")
    )
    return final_df

def run_pipeline():
    df = load_data()
    if df is None:
        return
    clean_rows, bad_rows = validate_data(df)
    
    final_df = aggregate_data(clean_rows)
    final_df.toPandas().to_csv("output.csv", index=False)
    print(f"[AGGREGATE] {final_df.count()} products aggregated")
    clean_rows.toPandas().to_csv("clean_data.csv", index=False)
    bad_rows.toPandas().to_csv("bad_data.csv", index=False)

    print(f"[OUTPUT] clean_data.csv : {clean_rows.count()} rows")
    print(f"[OUTPUT] bad_rows.csv : {bad_rows.count()} rows")

    

run_pipeline()