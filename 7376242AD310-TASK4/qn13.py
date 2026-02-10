purchases = {"Alice": 12000, "Bob": 7000, "Charlie": 3000}
final_amounts = {}

for name, amount in purchases.items():
    if amount > 10000:
        final_price = amount * 0.8
    elif amount > 5000:
        final_price = amount * 0.9
    else:
        final_price = amount
    final_amounts[name] = final_price

print(final_amounts)
