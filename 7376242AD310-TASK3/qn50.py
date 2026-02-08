n=int(input())
lst=[]
for i in range(n):
    d={}
    m=int(input())
    for j in range(m):
        k=input()
        v=input()
        d[k]=v
    lst.append(d)
summary={"rows":n,"unique_values":{}}
for k in lst[0]:
    vals=set()
    for d in lst:
        vals.add(d[k])
    summary["unique_values"][k]=len(vals)
print(summary)
