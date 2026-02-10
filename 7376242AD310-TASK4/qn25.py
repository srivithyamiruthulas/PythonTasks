sales = [
    {"item": "Laptop", "cat": "Elec", "price": 50000},
    {"item": "Shirt", "cat": "Cloth", "price": 2000},
    {"item": "Phone", "cat": "Elec", "price": 20000}
]

cat_sales = {}
for s in sales:
    c = s["cat"]
    cat_sales[c] = cat_sales.get(c, 0) + s["price"]

print(cat_sales)
