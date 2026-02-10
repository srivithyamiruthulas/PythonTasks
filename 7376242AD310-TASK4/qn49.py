orders = [{"id": 1, "rest": "R1", "items": ["A", "B", "A"]}, {"id": 2, "rest": "R2", "items": []}]

has_items = all(len(o["items"]) > 0 for o in orders)
dup_rest = {o["rest"] for o in orders if len(o["items"]) != len(set(o["items"]))}

print(has_items)
print(dup_rest)
