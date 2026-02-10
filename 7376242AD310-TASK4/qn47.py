devices = {"D1": [2, 3, 5], "D2": [1, 1]}

total_hours = {d: sum(h) for d, h in devices.items()}
avg_all = sum(total_hours.values()) / len(total_hours)
above_avg = [d for d, total in total_hours.items() if total > avg_all]

print(total_hours)
print(above_avg)
