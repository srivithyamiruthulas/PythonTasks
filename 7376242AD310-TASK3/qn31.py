n=int(input())
vocab=set()
for i in range(n):
    s=input().lower().split()
    for w in s:
        vocab.add(w)
print(vocab)
