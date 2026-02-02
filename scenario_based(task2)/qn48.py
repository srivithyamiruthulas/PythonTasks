num=int(input())
num1=int(input())
num2=num
c=0
while num2!=0:
    r=num2%10
    if r==num1:
        c=c+1
    num2=num2//10
print(c)