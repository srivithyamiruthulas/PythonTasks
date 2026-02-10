traffic = [[10, 20, 30], [40, 50, 60], [5, 15, 25]]

junction_totals = [sum(row) for row in traffic]
max_junction = junction_totals.index(max(junction_totals))

hourly_totals = [sum(col) for col in zip(*traffic)]
max_hour = hourly_totals.index(max(hourly_totals))

print(max_junction)
print(max_hour)
