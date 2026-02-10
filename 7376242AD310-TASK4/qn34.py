reviews = [
    {"id": 1, "sentiment": "Positive"},
    {"id": 2, "sentiment": "Negative"},
    {"id": 3, "sentiment": "Positive"}
]

counts = {}
for r in reviews:
    s = r["sentiment"]
    counts[s] = counts.get(s, 0) + 1

max_sentiment = max(counts, key=counts.get)

print(counts)
print(max_sentiment)
