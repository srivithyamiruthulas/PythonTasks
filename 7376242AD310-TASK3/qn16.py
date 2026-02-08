n=int(input())
lst=[]
while (n!=0):
    num=n%10
    n=n//10
    lst.append(num)
new=[]
for i in range(10):
    if i not in lst:
        new.append(i)
print(new)