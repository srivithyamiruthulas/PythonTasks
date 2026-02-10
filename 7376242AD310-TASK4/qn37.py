prefs = {
    "Alice": {"Bob", "Charlie"},
    "Bob": {"Alice"},
    "Charlie": {"Alice"},
    "Dave": set()
}

mutual = []
for s1, chosen in prefs.items():
    for s2 in chosen:
        if s2 in prefs and s1 in prefs[s2]:
            if (s2, s1) not in mutual:
                mutual.append((s1, s2))

all_chosen = set().union(*prefs.values())
isolated = [s for s in prefs if s not in all_chosen]

print(mutual)
print(isolated)
