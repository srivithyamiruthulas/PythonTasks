num=int(input())
num1=num
s=0
while num1!=0:
    r=num1%10
    s=s+r
    num1=num1//10
if s%9==0:
    print("VALID")
else:
    print("INVALID")