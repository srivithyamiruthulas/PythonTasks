n=int(input("Enter the number:"))
list1=[]
for i in range(1,n+1):
    inp=int(input("Enter num:"))
    list1.append(inp)
    
new_list=[]

for i in range(n):
    freq=0
    for j in range(n):
        if(list1[i]==list1[j]):
            freq+=1
    if(freq==1):
        new_list.append(list1[i])
print(new_list)
print(list1)
