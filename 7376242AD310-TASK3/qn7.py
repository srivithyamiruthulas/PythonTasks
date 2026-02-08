lst=[[1,2,3,4],[2,3],[5,4]]
list1=[]
for i in range(len(lst)):
    n=len(lst[i])
    for j in range(n):
        a=lst[i][j]
        list1.append(a)
print(list1)