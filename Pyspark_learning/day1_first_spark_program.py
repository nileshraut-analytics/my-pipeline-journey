
from pyspark.sql import SparkSession

# Create a Spark Session
spark = SparkSession.builder \
    .appName("My Pipeline Journey") \
    .getOrCreate()

# Sample data
data = [
    ("Alice", 25),
    ("Bob", 30),
    ("Charlie", 28)
]

# Column names
columns = ["name", "age"]

# Create Spark DataFrame
df = spark.createDataFrame(data, columns)

# Display the DataFrame
df.show()

# Stop the Spark Session
spark.stop()