delays = {
    "F1": [10, 20, 0],
    "F2": [45, 30],
    "F3": [5, 10, 5, 10]
}

avg_delays = {f: sum(d)/len(d) for f, d in delays.items()}
highest_delay_flight = max(avg_delays, key=avg_delays.get)

print(avg_delays)
print(highest_delay_flight)
