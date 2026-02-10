docs = [
    {"doc_id": 1, "tags": ["work", "urgent"]},
    {"doc_id": 2, "tags": ["work"]},
    {"doc_id": 3, "tags": ["work", "notes"]}
]

all_have_tags = all(len(d["tags"]) > 0 for d in docs)

common_tags = set(docs[0]["tags"])
for d in docs[1:]:
    common_tags = common_tags.intersection(d["tags"])

print(all_have_tags)
print(common_tags)
