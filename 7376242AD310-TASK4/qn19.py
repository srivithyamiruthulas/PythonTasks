readings = [
    {"temp": 25, "hum": 60},
    {"temp": 26},
    {"temp": 24, "hum": 62}
]

expected_keys = set(readings[0].keys())
faulty = []
valid = True

for i, r in enumerate(readings):
    if set(r.keys()) != expected_keys:
        faulty.append(i)
        valid = False

print("Consistency:", valid)
print("Faulty Indices:", faulty)
