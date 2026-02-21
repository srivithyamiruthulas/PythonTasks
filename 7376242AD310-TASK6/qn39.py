class Shipment:
    def delivery_time(self):
        pass

class AirShipment(Shipment):
    def delivery_time(self):
        print("2 days")

a = AirShipment()
a.delivery_time()