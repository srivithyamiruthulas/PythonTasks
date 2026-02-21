class Spread:
    def __init__(self, data):
        self.data = data

    def calculate(self):
        mean = sum(self.data) / len(self.data)
        variance = sum((x - mean) ** 2 for x in self.data) / len(self.data)
        return variance


numbers = [10, 20, 30, 40, 50]
s = Spread(numbers)
print("Variance:", s.calculate())