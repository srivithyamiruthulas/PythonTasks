num1=int(input("Enter a number:"))
num2=int(input("Enter 2nd number:"))
num3=int(input("Enter 3rd number:"))

if(num1>num2):
    if(num1>num3):
        print(f"{num1} is greater than {num2} and {num3}")
    else:
        print(f"{num3} is greater than {num1} and {num3}")
elif (num1==num2==num3):
    print("All the numbers are equal.")
else:
    pass
