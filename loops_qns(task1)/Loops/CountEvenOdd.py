n=int(input("Enter the n value:"))
if(n>=0):
    while(n!=0):
        digit=n%10
        n=n/10
        if(digit%2==0):
            evenSum+=digit
        else:
            oddSum+=digit
print(f"The Even digits count is {evenSum}/n the odd digit's sum is {oddSum}.")