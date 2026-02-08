n=int(input("Enter the number:"))
list1=[]
for i in range(1,n+1):
    inp=int(input("Enter num:"))
    list1.append(inp)
    
tar=int(input("Enter the target value:"))

for i in range(n):
    for j in range(n):
        if(list1[i]+list1[j]==tar and i<j):
            print(f"{list1[i]},{list1[j]}")