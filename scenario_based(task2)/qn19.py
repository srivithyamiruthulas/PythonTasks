num=int(input())
num1=num
rev=0
while num1!=0:
    n=num1%10
    rev=rev*10+n
    num1=num1//10
i=2
f=0
while i<=rev//2:
    if rev%i==0:
        f=1
        break
    i=i+1
if rev>1 and f==0:
    print("PRIME")
else:
    print("NOT PRIME")
