import logging
import logger
import pandas as pd
from extract import get_timestamp

def validate_data(df):
    df["amount"] = pd.to_numeric(df["amount"],errors="coerce")
    df["product"] = df["product"].str.strip().str.lower()
    bad_rows = df[df.isnull().any(axis = 1)].copy()
    clean_rows = df.dropna().copy()
    print(f"{get_timestamp()} [VALIDATE]  found {len(bad_rows)} bad rows")
    logging.info(f"[VALIDATE]  found {len(bad_rows)} bad rows")
    print(f"{get_timestamp()} [VALIDATE]  found {len(clean_rows)} clean rows\n")
    logging.info(f"[VALIDATE]  found {len(clean_rows)} clean rows")
    return bad_rows, clean_rows

def aggregate_data(clean_rows):
    final_df = clean_rows.groupby("product")["amount"].agg(
        count = "count",
        total = "sum",
        max = "max",
        min = "min"
    ).reset_index()
    print(f"{get_timestamp()} [AGGREGATE] Aggregated {len(final_df)} products from {len(clean_rows)} rows\n")
    logging.info(f"[AGGREGATE] Aggregated {len(final_df)} products from {len(clean_rows)} rows")
    return final_df