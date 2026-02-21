class Food:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Veg(Food):
    def final_price(self):
        return self.price

class NonVeg(Food):
    def final_price(self):
        return self.price + 20


f = NonVeg("Chicken", 150)
print("Bill:", f.final_price())