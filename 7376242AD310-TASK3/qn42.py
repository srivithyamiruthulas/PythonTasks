n=int(input())
lst=[]
for i in range(n):
    name=input()
    dept=input()
    marks=int(input())
    lst.append({"name":name,"dept":dept,"marks":marks})
res={}
for d in lst:
    dept=d["dept"]
    if dept not in res or d["marks"]>res[dept][1]:
        res[dept]=(d["name"],d["marks"])
print(res)
