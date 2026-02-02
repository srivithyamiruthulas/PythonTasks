num=int(input("Enter the no. of units:"))
while num!=0:
    if(num<=100):
        cost=2 
    elif(num<200):
        cost=100*2 + (num-100)*5 
    elif(num<400):
        cost=100*2 + (num-100)*5 + (num-300)*10
    else:
        pass
print(f"The total Cost:{cost}")