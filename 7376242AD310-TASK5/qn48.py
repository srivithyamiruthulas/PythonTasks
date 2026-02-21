class Average:
    def __init__(self, data):
        self.data = data

    def calculate(self):
        return sum(self.data) / len(self.data)


numbers = [10, 20, 30, 40, 50]
a = Average(numbers)
print("Average:", a.calculate())