n=int(input("Enter the n value:"))
if(n>0 & n%2==0):
    for i in range (0,n+1,2):
        sum=sum+n
print(f"The sum of n even Natural number is {sum}.")
