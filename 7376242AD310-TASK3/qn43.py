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
dups=[]
for i in range(len(lst)):
    for j in range(i+1,len(lst)):
        if lst[i]==lst[j]:
            dups.append(lst[i])
print(dups)
