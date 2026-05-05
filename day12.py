import pandas as pd

df = pd.read_csv("sales_input.csv")
print("===RAW DATA===")
print(df)

df["amount"] = pd.to_numeric(df["amount"],errors="coerce")
bad_df = df[df.isnull().any(axis=1)].copy()
clean_df = df.dropna().copy()

print("\n===BAD ROWS===")
print(bad_df)

print("\n===CLEAN ROWS===")
print(clean_df)

df2 = clean_df.groupby("product")["amount"].agg(["count","sum","max","min"])
print(df2)

df2.to_csv("new_output.csv",index=True)
bad_df.to_csv("errors_log.csv",index=True)