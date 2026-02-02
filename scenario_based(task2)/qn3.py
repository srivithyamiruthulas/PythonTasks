num=int(input())
num1=num
sum1=0
last=num % 10

while num1 > 0:
    n=num1 % 10
    sum1+=n
    num1//=10

if sum1%3==0 and last%2==0:
    print("VALID")
else:
    print("INVALID")
