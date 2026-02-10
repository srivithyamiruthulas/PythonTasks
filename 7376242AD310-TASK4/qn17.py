students = [
    {"name": "A", "dept": "CS", "cgpa": 8.5},
    {"name": "B", "dept": "CS", "cgpa": 7.5},
    {"name": "C", "dept": "IT", "cgpa": 9.0}
]

dept_data = {}
for s in students:
    d = s["dept"]
    if d not in dept_data:
        dept_data[d] = []
    dept_data[d].append(s["cgpa"])

dept_avg = {d: sum(g)/len(g) for d, g in dept_data.items()}

print(dept_avg)
