orders = ["Pizza", "Pasta", "Pizza", "Salad", "Pasta", "Burger"]

counts = {}
for dish in orders:
    counts[dish] = counts.get(dish, 0) + 1

most_ordered = max(counts, key=counts.get)

once = [dish for dish, count in counts.items() if count == 1]

print(most_ordered)
print(once)
