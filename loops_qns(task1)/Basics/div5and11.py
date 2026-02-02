num=int(input("Enter a number:"))
if num>0:
    if ((num%5==0) & (num%11==0)):
        print("Divisible")
    else:
        print("Not Divisible")
        