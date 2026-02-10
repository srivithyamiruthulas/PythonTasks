num=int(input("Enter the no of student's details to be entered:"))
dict1={}
for i in range(num):
    key=int(input("Enter a key:"))
    n=int(input("Enter the no of modules completed"))
    list2=[]
    list2.append(n)
    list1=[]
    for j in range(n):
        value=input("Enter the modules completed:")
        list1.append(value)
        dict1[key]=list1
    maxx=max(list2)
    ind=list2.index(maxx)

key_lst=list(dict1)
target_key=key_lst[ind]
print(f"{target_key} completed the max number of modules of {maxx}")

print("list of modules each student completed: ")
for key, value in dict1.items():
    print(f"{key} : {value}")