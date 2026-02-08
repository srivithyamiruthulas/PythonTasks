n=int(input())
lst=[]
for i in range(n):
    name=input()
    marks=int(input())
    att=int(input())
    lst.append({"name":name,"marks":marks,"attendance":att})
res={}
topper=""
top_val=0
for d in lst:
    idx=d["marks"]*0.7+d["attendance"]*0.3
    res[d["name"]]=idx
    if idx>top_val:
        top_val=idx
        topper=d["name"]
print(res)
print(topper)
