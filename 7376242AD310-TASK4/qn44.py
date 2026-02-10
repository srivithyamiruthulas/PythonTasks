usage = {"U1": [500, 200, 400], "U2": [1000, 1200]}
limit = 1500

exceeded = [u for u, data in usage.items() if sum(data) > limit]
avg_usage = {u: sum(data)/len(data) for u, data in usage.items()}
highest_avg_user = max(avg_usage, key=avg_usage.get)

print(exceeded)
print(highest_avg_user)
