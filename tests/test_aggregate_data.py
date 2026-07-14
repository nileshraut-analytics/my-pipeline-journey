import sys
import os

# lets Python find Pyspark_learning/day8_connected_postgres.py from inside tests/
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "Pyspark_learning"))

import pytest
from pyspark.sql import SparkSession
from day8_connected_postgres import aggregate_data


@pytest.fixture(scope="module")
def spark():
    # one SparkSession shared across all tests in this file
    spark = SparkSession.builder.appName("TestAggregateData").getOrCreate()
    yield spark
    spark.stop()


def test_aggregate_data_basic(spark):
    # fake input: 2 rows of "apple" (10, 20), 1 row of "banana" (5)
    data = [
        ("apple", 10.0),
        ("apple", 20.0),
        ("banana", 5.0),
    ]
    df = spark.createDataFrame(data, ["product", "amount"])
    clean_rows_count = df.count()  # 3

    result_df, final_df_count = aggregate_data(df, clean_rows_count)
    result = {row["product"]: row for row in result_df.collect()}

    # apple: 2 rows, sum=30, max=20, min=10, avg=15
    assert result["apple"]["product_count"] == 2
    assert result["apple"]["total_sales"] == 30.0
    assert result["apple"]["max_amount"] == 20.0
    assert result["apple"]["min_amount"] == 10.0
    assert result["apple"]["avg_amount"] == 15.0

    # banana: 1 row, sum=5, max=5, min=5, avg=5
    assert result["banana"]["product_count"] == 1
    assert result["banana"]["total_sales"] == 5.0

    # 2 unique products
    assert final_df_count == 2