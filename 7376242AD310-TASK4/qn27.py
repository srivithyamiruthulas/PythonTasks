enrollments = {"Python": {"S1", "S2"}, "Java": {"S2", "S3"}, "SQL": {"S1", "S2", "S4"}}

counts = {}
for students in enrollments.values():
    for sid in students:
        counts[sid] = counts.get(sid, 0) + 1

multi_course = [sid for sid, c in counts.items() if c > 1]

max_enroll = max(len(s) for s in enrollments.values())
top_courses = [c for c, s in enrollments.items() if len(s) == max_enroll]

print(multi_course)
print(top_courses)
