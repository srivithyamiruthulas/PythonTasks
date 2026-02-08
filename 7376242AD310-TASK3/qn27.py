a=list(map(int,input().split()))
b=list(map(int,input().split()))
flag=False
for i in range(len(a)):
    if a==b:
        flag=True
        break
    a=a[1:]+[a[0]]
print(flag)
