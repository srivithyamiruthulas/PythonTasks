import math

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    
    def area(self):
        return self.length * self.breadth

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5 * self.base * self.height


print("1. Circle")
print("2. Rectangle")
print("3. Triangle")

choice = int(input("Choose shape: "))

if choice == 1:
    r = float(input("Enter radius: "))
    shape = Circle(r)

elif choice == 2:
    l = float(input("Enter length: "))
    b = float(input("Enter breadth: "))
    shape = Rectangle(l, b)

elif choice == 3:
    b = float(input("Enter base: "))
    h = float(input("Enter height: "))
    shape = Triangle(b, h)

else:
    print("Invalid choice")
    exit()

print("Area:", shape.area())