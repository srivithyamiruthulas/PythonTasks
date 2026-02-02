num = int(input())
c=0
i=1
while i<=num:
    num1=i
    f=0
    while num1!=0:
        n=num1%10
        if n==4:
            f=1
            break
        num1=num1//10    
    if f==0:
        c=c+1
    i=i+1
print(c)