import math

class LogRatio:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculate(self):
        return math.log(self.a / self.b)


a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

l = LogRatio(a, b)
print("Log value:", l.calculate())