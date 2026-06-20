from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = SparkSession.builder.appName("File Handling").getOrCreate()

df = spark.read.csv("sales_input.csv", header=True)

final_df = df.groupBy("product").agg(
    F.count("product").alias("product_count"),
    F.sum("price").alias("total_price"),
    F.max("price").alias("max_amount"),
    F.min("price").alias("min_amount"),
    F.avg("price").alias("average_amount")
)

final_df.toPandas().to_csv("output.csv", index=False)

