doc1 = ["data", "science", "python", "code"]
doc2 = ["python", "code", "logic", "data"]

set1, set2 = set(doc1), set(doc2)
intersection = set1.intersection(set2)
union = set1.union(set2)

jaccard = len(intersection) / len(union)
is_similar = jaccard >= 0.5

print(jaccard)
print(is_similar)
