stops = [10, 25, 15, 30, 5]

max_passengers = max(stops)
max_stop_index = stops.index(max_passengers)

avg = sum(stops) / len(stops)
below_avg_stops = [i for i, count in enumerate(stops) if count < avg]

print(max_stop_index)
print(below_avg_stops)
