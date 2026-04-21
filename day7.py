import pandas as pd

df = pd.read_csv("sales_input.csv")
df["amount"] = pd.to_numeric(df["amount"], errors = "coerce")
print(df)
print(df.dtypes)
