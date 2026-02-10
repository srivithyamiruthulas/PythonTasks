reservations = [("A1", 10), ("B2", 5), ("A1", 10), ("A1", 15), ("B2", 5), ("C3", 1)]

seen = set()
duplicates = []
for res in reservations:
    if res in seen:
        if res not in duplicates:
            duplicates.append(res)
    seen.add(res)

coach_counts = {}
unique_seats = set(reservations)
for coach, seat in unique_seats:
    coach_counts[coach] = coach_counts.get(coach, 0) + 1

print(duplicates)
print(coach_counts)
