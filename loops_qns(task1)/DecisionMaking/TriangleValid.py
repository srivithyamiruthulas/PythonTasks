side1=int(input("Enter 1st side:"))
side2=int(input("Enter 2nd side"))
side3=int(input("Enter 3rd side:"))
if((side1,side2,side3)>0):
    if(side1==side2==side3):
        print("Equilateral Triangle")
    elif((side1==side2)| (side2==side3) | (side1==side3)):
        print("Isoceles Triangle")
    else:
        print("Scalane Triangle")
else:
    print("Invalid Input!")