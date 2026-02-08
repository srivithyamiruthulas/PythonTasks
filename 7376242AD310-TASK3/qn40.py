n=int(input())
lst=[]
for i in range(n):
    d={}
    m=int(input())
    for j in range(m):
        key=input()
        val=input()
        d[key]=val
    lst.append(d)
flag=True
keys=set(lst[0].keys())
for d in lst:
    if set(d.keys())!=keys:
        flag=False
print(flag)
