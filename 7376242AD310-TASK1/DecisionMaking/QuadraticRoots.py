a=int(input("enter a:"))
b=int(input("enter b:"))
c=int(input("enter c:"))
d=b**2-4*a*c
if(d>0):
    print("real and distinct roots!")
elif(d==0):
    print("real and equal roots!")
else:
    print("Imaginary roots!")