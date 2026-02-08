data=list(map(int,input().split()))
rem=list(map(int,input().split()))
res=[]
for i in data:
    if i not in rem:
        res.append(i)
print(res)
