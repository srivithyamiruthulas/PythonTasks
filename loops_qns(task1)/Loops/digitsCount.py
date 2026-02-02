n=int(input("Enter the n value:"))
if(n>=0):
    while(n!=0):
        n=n/10
        c+=1
        sum=sum+c
print(f"The digits count is {sum}.")