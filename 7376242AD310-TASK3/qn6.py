r=int(input())
c=int(input())
mat=[]
for i in range(r):
    mat.append(list(map(int,input().split())))
colsum=[0]*c
for i in range(r):
    for j in range(c):
        colsum[j]+=mat[i][j]
print(colsum)