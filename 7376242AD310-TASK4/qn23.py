logs = [(101, "09:00"), (102, "09:15"), (101, "09:00"), (103, "09:30")]

seen = set()
invalid = []

for entry in logs:
    if entry in seen:
        invalid.append(entry)
    else:
        seen.add(entry)

print(invalid)
