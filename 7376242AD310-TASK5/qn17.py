class Bill:
    def __init__(self, units):
        self.units = units

class Electricity(Bill):
    def amount(self):
        return self.units * 6

class Water(Bill):
    def amount(self):
        return self.units * 3


b = Electricity(100)
print("Bill:", b.amount())