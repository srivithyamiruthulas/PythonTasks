num=int(input())
num1=num
sum1=0
p=1
while num1!=0:
    n=num1%10
    sum1=sum1+n
    p=p*n
    num1=num1//10
if sum1%2==0 and p%3==0:
    print("VALID")
else:
    print("INVALID")
