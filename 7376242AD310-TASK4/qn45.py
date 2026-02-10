inventory = [
    {"id": 1, "cat": "A", "stock": 10},
    {"id": 2, "cat": "B", "stock": 0}
]

all_positive = all(p["stock"] > 0 for p in inventory)
out_of_stock_cats = {p["cat"] for p in inventory if p["stock"] == 0}

print(all_positive)
print(out_of_stock_cats)
