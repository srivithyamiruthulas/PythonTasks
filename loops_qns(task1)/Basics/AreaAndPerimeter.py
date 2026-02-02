shape=str(input("Enter any of the shape(rectangle/circle):"))
if(shape.lower() == "rectangle"):
    length=float(input("Enter the length of the rectangle:"))
    breath=float(input("Enter the breath of the rectangle:"))
    perimeter=2*(length+breath)
    print(f"The perimeter of the Rectangle is {perimeter}")
elif (shape.lower() == "circle"):
    r=float(input("Enter the Radius of the circle:"))
    circumference=3.14*2*r
    area=3.14*r**2
    print(f"The circumference of the Circle is {circumference}")
    print(f"The area of the Circle is {area}")
else:
    print("Please enter a valid shape!")
print("the parameters are calculated...")