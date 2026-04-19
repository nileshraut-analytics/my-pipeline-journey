# print("Subha Naba Barsha!")
# print("Day-2: I showed up again.")

sales = [
    {"product" : "apple","amount" : 100},
    {"product" : "banana","amount" : 50}
]

result = {}

for sale in sales:
    product = sale["product"]
    amount = sale["amount"]

    if product not in result:
        result[product] = {"count" : 0,"total" : 0,"max" : amount,"min" : amount}
    result[product]["count"] += 1
    result[product]["total"] += amount
    result[product]["max"] = max(result[product]["max"],amount)
    result[product]["min"] = min(result[product]["min"],amount)

print(result)
