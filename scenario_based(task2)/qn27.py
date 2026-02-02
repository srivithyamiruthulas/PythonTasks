num=int(input())
num1=int(input())
c=0
if num<20:
    print(0)
else:
    while num>=20:
        num=num-num1
        c=c+1
    print(c)