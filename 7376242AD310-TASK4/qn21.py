attempts = {"Alice": [1, 2, 3], "Bob": [2, 3, 4], "Charlie": [1, 2, 3, 4]}

# Total unique questions
all_questions = set().union(*(set(q) for q in attempts.values()))

# Students who attempted all unique questions
completed_all = [n for n, q in attempts.items() if set(q) == all_questions]

print(all_questions)
print(completed_all)
