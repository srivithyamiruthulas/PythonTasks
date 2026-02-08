#Remove Consecutive Duplicates
lst=[1,2,3,4,4,5,5,5,2,1,1,1]
n=len(lst)
for i in range(n-1,0,-1):
    if(lst[i]==lst[i-1]):
        lst.pop(i)
print(lst)