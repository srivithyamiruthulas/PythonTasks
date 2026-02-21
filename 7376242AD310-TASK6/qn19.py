class Delivery:
    def dispatch(self):
        pass

class BikeDelivery(Delivery):
    def dispatch(self):
        print("Dispatched by Bike")

d = BikeDelivery()
d.dispatch()