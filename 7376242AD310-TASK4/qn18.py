files = ["img.jpg", "doc.pdf", "script.py", "photo.jpg", "data.csv"]

organized = {}
for f in files:
    ext = f.split(".")[-1]
    if ext not in organized:
        organized[ext] = []
    organized[ext].append(f)

print(organized)
