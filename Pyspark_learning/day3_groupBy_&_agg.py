from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = SparkSession.builder.appName("My Pipeline Journey").getOrCreate()

data = [
    ("Alice", 25, "HR", 45000),
    ("Bob", 30, "IT", 60000),
    ("Charlie", 28, "Finance", 55000),
    ("David", 35, "IT", 70000),
    ("Eva", 26, "HR", 48000)
]

columns = ["Name", "Age", "Department", "Salary"]

df = spark.createDataFrame(data, columns)

# df.groupBy("Department").agg({"Salary" : "avg"}).show()
df.groupBy("Department").agg(
    F.count("Salary").alias("count_salary"),
    F.sum("Salary").alias("total_salary"),
    F.max("Salary").alias("max_salary"),
    F.min("Salary").alias("min_salary"),
    F.avg("Salary").alias("average_salary")
).show()

spark.stop()

