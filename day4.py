sales = [{"product" : "apple","amount" : 100},
         {"product" : "banana","amount" : 50},
         {"product" : "apple","amount" : 30},
         {"product" : "apple","amount" : None},
         {"product" : "banana","amount" : "abc"},
         {"product" : None,"amount" : 40},
         {"product" : "orange","amount" : "60"}
         ]

result = {}
errors = []

def clean_value(value,product):
    try:
        return int(value)
    except(ValueError,TypeError):
        errors.append({
            "product" : product,
            "value" : value
        })
        return None
    
for sale in sales:
    product = sale["product"]
    amount = clean_value(sale["amount"],product)

    if product is None:
        errors.append({"bad record" : sale, "reason" : "missing product"})
        continue
    
    if amount is None:
        continue

    if product not in result:
        result[product] = {"count" : 0,"total" : 0,"max" : amount,"min" : amount}
    result[product]["count"] += 1
    result[product]["total"] += amount
    result[product]["max"] = max(result[product]["max"],amount)
    result[product]["min"] = min(result[product]["min"],amount)

print(result)
print(errors)

with open("new_output.csv","w") as file:
    file.write("product,count,total,max,min\n")
    for product, data in result.items():
        file.write(f"{product},{data['count']},{data['total']},{data['max']},{data['min']}\n")

print("CSV saved!")