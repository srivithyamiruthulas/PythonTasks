n=int(input("Enter the n value:"))
nc=n
if(n>0):
    while(n!=0):
        digit=n%10
        n=n//10
        rev=rev*10+digit
    print(f"The reversed number: {rev}.")
else:
    print("invalid input")