scores_data = {
    "Alice": [85, 90, 88],
    "Bob": [70, 65, 72],
    "Charlie": [95, 92, 98],
    "Dave": [60, 70, 68]
}

student_averages = {name: sum(scores) / len(scores) for name, scores in scores_data.items()}
class_avg = sum(student_averages.values()) / len(student_averages)
top_students = [name for name, avg in student_averages.items() if avg > class_avg]

print(student_averages)
print(top_students)
