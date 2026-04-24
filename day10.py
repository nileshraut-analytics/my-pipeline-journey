import pandas as pd

# ----------------------
# TASK 1: VALIDATION PIPELINE
# ----------------------
raw_df = pd.read_csv("sales_input.csv")

raw_df["amount"] = pd.to_numeric(raw_df["amount"], errors="coerce")

bad_rows = raw_df[raw_df.isnull().any(axis=1)]
clean_rows = raw_df.dropna()

print("\n=== BAD ROWS ===")
print(bad_rows)

print("\n=== CLEAN ROWS ===")
print(clean_rows)


# ----------------------
# TASK 2: STRING CLEANING
# ----------------------
product_df = pd.DataFrame([
    {"product": "  Apple  ", "amount": 200},
    {"product": "BANANA", "amount": 70},
    {"product": "orange", "amount": 40}
])

product_df["product"] = product_df["product"].str.strip().str.lower()

print("\n=== CLEANED PRODUCTS ===")
print(product_df)


# ----------------------
# TASK 3: DUPLICATE HANDLING
# ----------------------
dup_df = pd.DataFrame({
    "product": [" Apple ", "apple", "BANANA", "banana ", " Mango", "mango", "APPLE"]
})

dup_df["product"] = dup_df["product"].str.strip().str.lower()

dup_df["is_duplicated"] = dup_df["product"].duplicated()

duplicates_df = dup_df[dup_df["is_duplicated"]]
unique_df = dup_df[~dup_df["is_duplicated"]]

print("\n=== DUPLICATES ===")
print(duplicates_df)

print("\n=== CLEAN DATA ===")
print(unique_df)