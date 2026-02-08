lst=list(map(int,input().split()))
flag=False
seen=set()
for i in lst:
    if i in seen:
        flag=True
        break
    seen.add(i)
print(flag)
