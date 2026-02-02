num1=0
num2=1
num=int(input("enter the limit:"))
for i in range(num):
    print(num1,end=" ")
    temp=num1+num2
    num1=num2
    num2=temp