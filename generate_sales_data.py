import pandas as pd
import random

products = {
    "Samsung Galaxy M14": "Electronics",
    "iPhone 15": "Electronics",
    "Boat Earbuds": "Electronics",
    "HP Laptop": "Electronics",
    "Dell Monitor": "Electronics",
    "Nike Shoes": "Fashion",
    "Adidas Shoes": "Fashion",
    "Levis Jeans": "Fashion",
    "Puma T-Shirt": "Fashion",
    "Study Table": "Furniture",
    "Office Chair": "Furniture",
    "Water Bottle": "Home"
}

cities = [
    "Kolkata", "Delhi", "Mumbai", "Bangalore",
    "Chennai", "Hyderabad", "Pune", "Jaipur",
    "Ahmedabad", "Lucknow"
]

payment_modes = [
    "UPI",
    "Credit Card",
    "Debit Card",
    "Net Banking",
    "Cash on Delivery"
]

data = []

for i in range(1, 501):
    product = random.choice(list(products.keys()))

    row = {
        "order_id": f"ORD{i:04}",
        "customer_id": f"CUST{random.randint(1000,9999)}",
        "product": product,
        "category": products[product],
        "city": random.choice(cities),
        "quantity": random.randint(1, 5),
        "amount": random.randint(500, 50000),
        "payment_mode": random.choice(payment_modes),
        "order_date": pd.Timestamp("2025-01-01") + pd.Timedelta(days=random.randint(0, 150))
    }

    data.append(row)

df = pd.DataFrame(data)

# Dirty data for pipeline testing
df.loc[10:19, "city"] = None
df.loc[30:39, "product"] = None
df.loc[50:59, "amount"] = "abc"

df.to_csv("amazon_sales_data.csv", index=False)

print("amazon_sales_data.csv created successfully")