from pyspark.sql import SparkSession

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
# df.show()
# df.printSchema()
# print(df.columns)
# print(df.dtypes)
# print(df.count())
df.select("name").show()
df.filter(df.Age>26).show()
spark.stop()

