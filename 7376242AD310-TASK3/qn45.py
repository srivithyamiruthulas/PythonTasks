req={}
n=int(input())
for i in range(n):
    k=input()
    v=int(input())
    req[k]=v
stu={}
m=int(input())
for i in range(m):
    k=input()
    v=int(input())
    stu[k]=v
score=0
for k in req:
    if k in stu:
        score+=req[k]*stu[k]
print(score)
