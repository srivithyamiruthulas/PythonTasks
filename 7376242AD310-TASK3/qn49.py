d={}
n=int(input())
for i in range(n):
    k=input()
    v=float(input())
    d[k]=v
total=sum(d.values())
for k in d:
    d[k]=d[k]/total
print(d)
