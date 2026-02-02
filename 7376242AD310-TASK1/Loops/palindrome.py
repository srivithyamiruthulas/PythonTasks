n=int(input("Enter the n value:"))
nc=n
if(n>0):
    rev=0
    while(n!=0):
        digit=n%10
        n=n//10
        rev=rev*10+digit
    if(nc==rev):
        print("Palindrome!")
    else:
        print("Not a palindrome!")  
else:
    print("invalid input")