num=int(input())
num1=num
f=0

while num1!=0:
    n=num1%10
    if n==0:
        f=1
        break
    num1=num1//10
if f==1 and num%10==5:
    print("OPEN")
else:
    print("LOCKED")
