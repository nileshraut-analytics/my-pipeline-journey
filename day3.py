# Day 3: Understanding Processing

sales = [
    {"product" : "apple","amount" : 100},
    {"product" : "banana","amount" : 50},
    {"product" : "apple","amount" : 30},
    {"product" : "apple","amount" : None},
    {"product" : "banana","amount" : "abc"},
    {"product" : None,"amount" : 40},
    {"product" : "orange","amount" : "60"}
]

result = {}
errors = []

def safe_amount(value, product):
    try:
        return int(value)
    except(ValueError, TypeError):
        errors.append({
            "product" : product,
            "bad_value" : value
        })
        return 0

for sale in sales:
    product = sale["product"]
    amount = safe_amount(sale["amount"], product)

    if product not in result:
        result[product] = {"count" : 0,"total" : 0,"max" : amount,"min" : amount}
    result[product]["count"] += 1
    result[product]["total"] += amount
    result[product]["max"] = max(result[product]["max"],amount)
    result[product]["min"] = min(result[product]["min"],amount)

print(result)