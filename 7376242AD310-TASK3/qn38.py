d={"A":"CSE","B":"ECE","C":"CSE"}
res={}
for k in d:
    v=d[k]
    if v in res:
        res[v].append(k)
    else:
        res[v]=[k]
print(res)
