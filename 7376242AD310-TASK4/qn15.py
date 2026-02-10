attendance = {"Alice": {"Mon", "Tue", "Wed"}, "Bob": {"Mon", "Wed"}, "Charlie": {"Mon", "Tue", "Wed"}}
working_days = {"Mon", "Tue", "Wed"}

total_days = {name: len(days) for name, days in attendance.items()}
perfect_attendance = [name for name, days in attendance.items() if days == working_days]

print(total_days)
print(perfect_attendance)
