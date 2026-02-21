class Payment:
    def pay(self, amount):
        pass

class CardPayment(Payment):
    def pay(self, amount):
        print("Paid", amount, "using Card")

class UPIPayment(Payment):
    def pay(self, amount):
        print("Paid", amount, "using UPI")

payment = CardPayment()
payment.pay(500)