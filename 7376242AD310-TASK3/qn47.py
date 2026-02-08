n=int(input())
lst=[]
for i in range(n):
    name=input()
    score=int(input())
    lst.append((name,score))
lst.sort(key=lambda x:x[1],reverse=True)
rank=1
prev=None
res={}
for i in range(len(lst)):
    if prev!=None and lst[i][1]!=prev:
        rank=i+1
    res[lst[i][0]]=rank
    prev=lst[i][1]
print(res)
