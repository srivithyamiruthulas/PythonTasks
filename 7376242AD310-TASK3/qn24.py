n=int(input())
mat=[]
for i in range(n):
    mat.append(list(map(int,input().split())))
p_sum=0
s_sum=0
for i in range(n):
    p_sum+=mat[i][i]
    s_sum+=mat[i][n-i-1]
print(p_sum)
print(s_sum)
