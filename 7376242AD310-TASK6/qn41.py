class Gateway:
    def process(self):
        pass

class Paytm(Gateway):
    def process(self):
        print("Payment successful")

p = Paytm()
p.process()