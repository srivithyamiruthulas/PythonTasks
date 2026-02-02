year=int(input("Enter the year:"))
if year>0:
    if(year % 4 == 0) & (year % 100 != 0):
        print("Leap year")
    elif(year % 400):
        print("Leap year")
    else:
        print("Not a leap year")
else:
    print("Not a leap year!")
    
    
    