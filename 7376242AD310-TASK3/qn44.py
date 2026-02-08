s=input().lower().split()
res={}
for i in range(len(s)-1):
    pair=(s[i],s[i+1])
    if pair in res:
        res[pair]+=1
    else:
        res[pair]=1
print(res)
