required = {"Python", "SQL", "Java", "Docker", "AWS"}
resumes = {
    "Alice": ["Python", "SQL", "Java"],
    "Bob": ["Python", "Docker", "AWS", "SQL", "Java"],
    "Charlie": ["C++", "Java"]
}

matches = []
missing = {}

for name, skills in resumes.items():
    skills_set = set(skills)
    found = skills_set.intersection(required)
    
    if (len(found) / len(required)) >= 0.7:
        matches.append(name)
    
    missing[name] = required - skills_set

print(matches)
print(missing)
