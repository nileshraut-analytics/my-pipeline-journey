
import csv

result = {}
errors = []

def clean_value(value,product):
    try:
        return int(value)
    except(ValueError,TypeError):
        errors.append({
            "product" : product,
            "value" : value,
            "reason" : "invalid amount"
        })
        return None
    
with open("sales_input.csv","r") as f:
    reader = csv.DictReader(f)
    for item in reader:
        product = item["product"]
        amount = clean_value(item["amount"],product)

        if not product:
            errors.append({
                "product" : "",
                "value" : item["amount"],
                "reason" : "missing product"
            })
            continue
    
        if amount is None:
            continue

        if product not in result:
            result[product] = {"count" : 0,"total" : 0,"max" : amount,"min" : amount}
        result[product]["count"] += 1
        result[product]["total"] += amount
        result[product]["max"] = max(result[product]["max"],amount)
        result[product]["min"] = min(result[product]["min"],amount)
        

with open("errors_log.csv","w") as f:
    f.write("product,amount,reason\n")
    for item in errors:
        f.write(f"{item['product']},{item['value']},{item['reason']}\n")


with open("new_output.csv","w") as file:
    file.write("product,count,total,max,min\n")
    for product, data in result.items():
        file.write(f"{product},{data['count']},{data['total']},{data['max']},{data['min']}\n")

print("CSV saved!")
