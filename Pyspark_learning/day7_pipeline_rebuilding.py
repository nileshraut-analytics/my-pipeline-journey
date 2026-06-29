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
    
df = load_data()
df.show()
