skills_data = {
    "Alice": {"Python", "SQL", "Java"},
    "Bob": {"Python", "C++"},
    "Charlie": {"Python", "SQL", "Tableau"},
    "Dave": {"SQL", "Java"}
}

both_python_sql = [name for name, skills in skills_data.items() if {"Python", "SQL"}.issubset(skills)]

at_least_one = set().union(*skills_data.values())

known_by_all = set.intersection(*skills_data.values())

print(both_python_sql)
print(at_least_one)
print(known_by_all)
