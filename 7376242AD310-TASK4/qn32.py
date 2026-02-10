resumes = {
    "Alice": [2, 3, 5],
    "Bob": [1, 2],
    "Charlie": [10, 2]
}

total_exp = {name: sum(exp) for name, exp in resumes.items()}
avg_exp = sum(total_exp.values()) / len(total_exp)
above_avg = [name for name, total in total_exp.items() if total > avg_exp]

print(total_exp)
print(above_avg)
