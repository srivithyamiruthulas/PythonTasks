from collections import Counter

borrowed_books = [
    {"student": "Alice", "book": "Python 101", "days": 10},
    {"student": "Bob", "book": "Data Science", "days": 5},
    {"student": "Charlie", "book": "Python 101", "days": 8},
    {"student": "Alice", "book": "Algos", "days": 12},
    {"student": "Dave", "book": "Data Science", "days": 3}
]

long_borrows = [record["student"] for record in borrowed_books if record["days"] > 7]
print(f"Students (7+ days): {set(long_borrows)}")

book_counts = Counter(record["book"] for record in borrowed_books)
print(f"Borrow frequency: {dict(book_counts)}")
