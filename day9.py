import pandas as pd

df = pd.read_csv("sales_input.csv")
df["amount"] = pd.to_numeric(df["amount"], errors="coerce")

bad_rows = df[df.isnull().any(axis = 1)]
clean_rows = df.dropna()

print("bad rows: ")
print(bad_rows)
print("\nclean rows")
print(clean_rows)
