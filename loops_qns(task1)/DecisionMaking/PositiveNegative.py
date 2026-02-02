num1=int(input("Enter the first number:"))
if(type(num1)=='int'):
    if(num1>0):
            print("Positive number")
    elif(num1==0):
        print("The number is Zero")
    else:
        print("Negative number")
else:
    print("Please enter the input only in integer type..")