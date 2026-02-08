def avg():
    sum=0
    n=len(tup)
    for i in range(n):
        sum+=tup[i]
        avg=sum/n
        return avg
def mini():
    mini=min(tup)
    return mini
def maxi():
    maxi=max(tup)
    return maxi

tup=[]
n=int(input("Enter how many elements to be added in the tuple: "))
for i in range(n):
    inp=int(input())
    tup.append(inp)
print(f"The maximum element in {tup} is {maxi()}")
print(f"The mimimum element in {tup} is {mini()}")
print(f"The average of {tup} is {avg()}")
