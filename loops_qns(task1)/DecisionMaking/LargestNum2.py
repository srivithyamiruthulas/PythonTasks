num1=int(input("Enter a number:"))
num2=int(input("Enter 2nd number:"))
if(type(num1)=='int') & (type(num2)=='int'):
    if(num1>num2):
        print(f"{num1} is greater than {num2}")
    elif (num1==num2):
        print("Both the numbers are equal.")
    else:
        print(f"{num2} is greater than {num2}")
else:
    print("Invalid Input type!")