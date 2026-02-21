class Wallet:
    def __init__(self):
        self.balance = 0

    def add_money(self, amount):
        self.balance += amount

class CardPayment(Wallet):
    def pay(self, amount):
        self.balance -= amount
        print("Paid using Card")

w = CardPayment()
w.add_money(1000)
w.pay(200)
print("Balance:", w.balance)