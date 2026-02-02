num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
if(type(num1 & num2)=='int'):
    if((num1 & num2)>0):
        if(num1%2==0):
            print("even number")
        else:
            print("Odd number")
    else:
        print("Please enter only positive number.")
else:
    print("Please enter the input only in integer type..")