class Median:
    def __init__(self, data):
        self.data = sorted(data)

    def calculate(self):
        n = len(self.data)
        mid = n // 2
        if n % 2 == 0:
            return (self.data[mid - 1] + self.data[mid]) / 2
        else:
            return self.data[mid]


numbers = [10, 30, 20, 50, 40]
m = Median(numbers)
print("Median:", m.calculate())