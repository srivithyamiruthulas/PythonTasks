num=int(input())
num1=num
c=0
f=0
while num1!=0:
    r=num1%10
    if r==7:
        f=1
    c=c+1
    num1=num1//10
if f==1 and c>=6:
    print("STRONG")
else:
    print("WEAK")