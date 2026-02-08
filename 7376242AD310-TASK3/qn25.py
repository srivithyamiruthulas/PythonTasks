r=int(input())
c=int(input())
mat=[]
for i in range(r):
    mat.append(list(map(int,input().split())))
flag=True
for row in mat:
    if len(row)!=len(set(row)):
        flag=False
print(flag)
