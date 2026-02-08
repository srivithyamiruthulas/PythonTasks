s=input().lower()
flag=True
for ch in "abcdefghijklmnopqrstuvwxyz":
    if ch not in s:
        flag=False
        break
print(flag)
