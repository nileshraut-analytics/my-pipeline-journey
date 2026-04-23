import pandas as pd

df = pd.read_csv("sales_input.csv")
df["amount"] = pd.to_numeric(df["amount"], errors="coerce")

#Task 1: show me only rows where product is "apple".
print(df.query("product == 'apple'"))

#Task 2: show me only rows where amount is greater than 50.
print(df.query("amount > 50"))

#Task 3
print(df.query("product == 'apple' and amount > 50"))

#Task 4: Filter where product is "apple" OR "orange"
print(df.query("product == 'apple' or product == 'orange'"))

#Task 5
filter_row = df.query("product == 'apple' or product == 'orange'")
print(filter_row["product"])
      