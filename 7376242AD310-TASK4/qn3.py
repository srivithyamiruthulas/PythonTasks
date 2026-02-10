from collections import Counter
lst = []
n = int(input("Enter the no of students to be registered: "))
for i in range(n):
    name = input(f"Enter name for student {i+1}: ")
    slot = input(f"Enter slot number for {name}: ")
    lst.append((name, slot))

all_names = [item[0] for item in lst]
all_slots = [item[1] for item in lst]

name_counts = Counter(all_names)
slot_counts = Counter(all_slots)

duplicate_names = [name for name, count in name_counts.items() if count > 1]
duplicate_slots = [slot for slot, count in slot_counts.items() if count > 1]

if not duplicate_names and not duplicate_slots:
    print("All assignments are valid.")
else:
    if duplicate_names:
        print(f"Invalid! These students appear more than once: {duplicate_names}")
    if duplicate_slots:
        print(f"Invalid! These slots are assigned to multiple students: {duplicate_slots}")
        