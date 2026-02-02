num=int(input("enter an even number:"))
num1=num
sum1=0
sum2=0
c=0
if(num>0 and num%2==0):
    while(num1!=0):
        n=num1%10
        num1=num1//10
        c=c+1
            
    d=c//2
    
    for i in range (d):
        n=num%10
        num=num//10
        sum1=sum1+n
    
    for i in range (d):
        n=num%10
        num=num//10
        sum2=sum2+n
        
    if(sum1==sum2):
        print("Balanced")
    else:
        print("Not Balanced")
        
else:
    print("Please enter a new number(odd number)")