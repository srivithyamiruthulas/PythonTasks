class Book:
    def __init__(self, price):
        self.__price = price

    def update_price(self, price):
        self.__price = price

b = Book(200)
b.update_price(250)