progress = {"S1": {1, 2, 3}, "S2": {1}, "S3": {1, 2, 3, 4}}
total_lessons = {1, 2, 3, 4}

completed_all = [s for s, p in progress.items() if p == total_lessons]
less_than_half = [s for s, p in progress.items() if len(p) < len(total_lessons) / 2]

print(completed_all)
print(less_than_half)
