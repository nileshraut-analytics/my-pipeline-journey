import pandas as pd

def load_data(filepath):
    df = pd.read_csv(filepath)
    print(f"loaded {len(df)} rows from {filepath}")
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
    print(f"Updating Data to Dedicted CSV File")
    return final_df.to_csv("new_output.csv", index=False)

def errors_log(bad_rows):
    print(f"Updating Data to Dedicted CSV File")
    return bad_rows.to_csv("errors_log.csv", index=False)

def run_pipeline(filepath):
    df = load_data(filepath)
    bad_rows, clean_rows = validate_data(df)
    final_df = aggregate_data(clean_rows)
    clean_output(final_df)
    errors_log(bad_rows)
    print("Pipeline Completed Successfully!")

run_pipeline("sales_input.csv")
