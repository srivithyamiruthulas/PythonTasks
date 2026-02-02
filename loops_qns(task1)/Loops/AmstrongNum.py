n=int(input("Enter the n value:"))
nc=n
if(n>0):
    rev=0
    while(n!=0):
        digit=n%10
        n=n//10
        rev=rev+digit**3
    if(nc==rev):
        print("Amstrong number!")
    else:
        print("Not an Amstrong number!")  
else:
    print("invalid input")