from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = SparkSession.builder.appName("File Handling").getOrCreate()

df = spark.read.csv("sales_input.csv", header=True)

def validate_data(df):
    clean_rows = df.na.drop()
    return clean_rows

def aggregate_data(df):
    final_df = validate_data(df).groupBy("product").agg(
        F.count("product").alias("product_count"),
        F.sum("price").alias("total_price"),
        F.max("price").alias("max_amount"),
        F.min("price").alias("min_amount"),
        F.avg("price").alias("average_amount")
    )
    return final_df


