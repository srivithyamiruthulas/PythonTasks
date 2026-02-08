n=int(input())
lst=[]
for i in range(n):
    name=input()
    score=int(input())
    lst.append((name,score))
lst.sort(key=lambda x:x[1],reverse=True)
print(lst)
