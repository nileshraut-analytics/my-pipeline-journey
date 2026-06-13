from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("First Spark Program").getOrCreate()
print(spark)