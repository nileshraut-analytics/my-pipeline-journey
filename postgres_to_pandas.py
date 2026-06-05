import psycopg2
import pandas as pd

conn = psycopg2.connect(
    host = "localhost",
    database = "Practice_database",
    user = "postgres",
    password = "Nilesh0424"
)

# cursor = conn.cursor()
# cursor.execute("SELECT product, SUM(amount) FROM sales GROUP BY product")
# rows = cursor.fetchall()
# df = pd.DataFrame(rows, columns=["product", "amount"])

def load_data():
    query = "SELECT * FROM sales"
    df = pd.read_sql(query, conn)
    print(f"Loaded {len(df)} rows from postgreSQL")
    return df

def validate_data(df):
    df["amount"] = pd.to_numeric(df["amount"],errors="coerce")
    df["product"] = df["product"].str.strip().str.lower()
    bad_rows = df[df.isnull().any(axis = 1)].copy()
    clean_rows = df.dropna().copy()
    print(f"loaded {len(bad_rows)} rows as Bad Data from Raw Data Source")
    print(f"loaded {len(clean_rows)} rows as Clean Data from Raw Data Source")
    return bad_rows, clean_rows

def aggregate_data(clean_rows):
    final_df = clean_rows.groupby("product")["amount"].agg(
        count = "count",
        total = "sum",
        max = "max",
        min = "min"
    ).reset_index()
    print(f"aggregated {len(final_df)} products from {len(clean_rows)} Clean Rows")
    return final_df

def clean_output(final_df):
    print(f"Writing clean output CSV")
    return final_df.to_csv("new_output.csv", index=False)

def errors_log(bad_rows):
    print(f"Writing errors log CSV")
    return bad_rows.to_csv("errors_log.csv", index=False)

def run_pipeline():
    df = load_data()
    bad_rows, clean_rows = validate_data(df)
    final_df = aggregate_data(clean_rows)
    clean_output(final_df)
    errors_log(bad_rows)
    print("Pipeline Completed Successfully!")

run_pipeline()
