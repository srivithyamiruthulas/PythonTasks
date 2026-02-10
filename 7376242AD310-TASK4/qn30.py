traffic_data = [
    [10, 20, 30],
    [5, 15, 10],
    [20, 25, 20]
]

junction_totals = [sum(row) for row in traffic_data]
max_junction = junction_totals.index(max(junction_totals))

hourly_totals = [sum(col) for col in zip(*traffic_data)]
max_hour = hourly_totals.index(max(hourly_totals))

print(max_junction)
print(max_hour)
