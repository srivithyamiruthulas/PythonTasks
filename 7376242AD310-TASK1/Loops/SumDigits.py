n=int(input("Enter the n value:"))
if(n>=0):
    while(n!=0):
        digit=n%10
        n=n/10
        sumDigits+=digit
print(f"The digits count is {sumDigits}.")