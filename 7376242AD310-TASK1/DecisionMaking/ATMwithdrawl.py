balance=int(input("Enter the balance amount:"))
amount=int(input("Enter the withdrawl amount:"))

if(amount % 100 == 0):
    if((amount+500) <= balance):
        print("success!")
    else:
        print("Rejection!")
else:
    print("The withdrawl Amount must be in the multiple of 100.")
    