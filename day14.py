# input --> processing, groupping, aggregation --> output

# read_csv
# grouping, aggregation, filter
# seggegation of clean_rows_csv and errors_Log

import pandas as pd
df = pd.read_csv("sales_input.csv")
df["amount"] = pd.to_numeric(df["amount"],errors="coerce")
bad_rows = df[df.isnull().any(axis=1)].copy()
clean_rows = df.dropna().copy()
final_output = clean_rows.groupby("product")["amount"].agg(
    count="count",
    total="sum",
    max="max",
    min="min"
).reset_index()

final_output.to_csv("new_output.csv",index = False)
bad_rows.to_csv("errors_log.csv",index=False)