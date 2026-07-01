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


df = df.withColumn("amount", F.expr("try_cast(amount as double)"))
df = df.withColumn("product", F.lower(F.trim(df["product"])))
clean_rows = df.na.drop()
bad_rows = df.subtract(clean_rows)
clean_rows.toPandas().to_csv("clean_data.csv", index=False)
bad_rows.toPandas().to_csv("bad_data.csv", index=False)

print(f"[OUTPUT] clean_data.csv : {clean_rows.count()} rows")
print(f"[OUTPUT] bad_rows.csv : {bad_rows.count()} rows")
