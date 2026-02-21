class Order:
    def __init__(self, order_id, customer, amount):
        self.order_id = order_id
        self.customer = customer
        self.amount = amount

class CreditCard(Order):
    def pay(self):
        print("Paid", self.amount, "using Credit Card")

class UPI(Order):
    def pay(self):
        print("Paid", self.amount, "using UPI")


o = CreditCard(101, "Sri", 500)
o.pay()