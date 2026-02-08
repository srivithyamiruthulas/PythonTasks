lst=input().split()
res={}
for w in lst:
    l=len(w)
    if l in res:
        res[l].append(w)
    else:
        res[l]=[w]
print(res)
