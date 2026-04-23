import pandas as pd

df = pd.read_csv("sales_input.csv")
df["amount"] = pd.to_numeric(df["amount"], errors="coerce")

# Real world: find apple sales with amount > 50
print(df.query("product == 'apple' and amount > 50"))