import pandas as pd

df = pd.read_csv("sales_input.csv")
df["amount"] = pd.to_numeric(df["amount"],errors="coerce")
clean_df = df.dropna().copy()

clean_df["rank"] = clean_df["amount"].rank(method="dense", ascending=False)

print(clean_df.sort_values("amount",ascending= False).reset_index(drop=True))