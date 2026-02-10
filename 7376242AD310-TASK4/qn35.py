logs = {
    "D1": ["ON", "OFF", "ON"],
    "D2": ["ON", "ON", "ON"],
    "D3": ["OFF", "OFF"]
}

ever_off = [d for d, s in logs.items() if "OFF" in s]
always_on = [d for d, s in logs.items() if all(v == "ON" for v in s)]

print(ever_off)
print(always_on)
