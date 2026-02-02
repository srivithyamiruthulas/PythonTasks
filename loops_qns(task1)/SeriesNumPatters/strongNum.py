nc=int(input("Enter the number:"))
summ=0
n=nc
while n!=0:
    num=n%10
    n=n//10
    
    sum=1
    while (num!=0):
        sum=sum*num
        num-=1
        
    summ=summ+sum
if(summ==nc):
    print("Strong number")
else:
    print("Not a strong number")