class Factorial:
    def __init__(self, num):
        self.num = num

    def calculate(self):
        fact = 1
        for i in range(1, self.num + 1):
            fact *= i
        return fact


num = int(input("Enter number: "))
f = Factorial(num)
print("Factorial:", f.calculate())