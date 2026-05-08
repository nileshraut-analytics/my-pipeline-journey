import pandas as pd
# INPUT
df = pd.read_csv("sales_input.csv")
# PROCESSING
# Step 1: Convert amount to numeric (handle bad data)
df["amount"] = pd.to_numeric(df["amount"], errors="coerce")

# Step 2: Separate bad and clean data
bad_df = df[df.isnull().any(axis=1)].copy()
clean_df = df.dropna().copy()

# Step 3: Aggregate clean data
result_df = clean_df.groupby("product")["amount"].agg(
    count="count",
    total="sum",
    max="max",
    min="min"
).reset_index()

# OUTPUT
# Save final result
result_df.to_csv("new_output.csv", index=False)

# Save error log
bad_df.to_csv("errors_log.csv", index=False)
