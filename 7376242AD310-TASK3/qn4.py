n=int(input("Enter the number: "))
list1=[]
for i in range(0,n):
    inp=int(input("Enter num: "))
    list1.append(inp)
print(list1)    

rot=int(input("Enter the no of rotations: "))
k=rot%n
rot_list=list1[:k]+list1[k:]

print("The right rotation after {rot} rotations is: ")    
print(rot_list)    
        
        