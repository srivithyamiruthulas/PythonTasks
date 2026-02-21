class Distance:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculate(self):
        return abs(self.a - self.b)


a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

d = Distance(a, b)
print("Distance:", d.calculate())