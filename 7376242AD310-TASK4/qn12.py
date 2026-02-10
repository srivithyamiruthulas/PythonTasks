votes = [(101, "A"), (102, "B"), (101, "B"), (103, "A"), (102, "A")]

voted_ids = set()
invalid_votes = []
final_counts = {}

for vid, candidate in votes:
    if vid in voted_ids:
        invalid_votes.append((vid, candidate))
    else:
        voted_ids.add(vid)
        final_counts[candidate] = final_counts.get(candidate, 0) + 1

print(invalid_votes)
print(final_counts)
