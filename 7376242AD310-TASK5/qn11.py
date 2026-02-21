class Ticket:
    def __init__(self, source, destination, distance):
        self.source = source
        self.destination = destination
        self.distance = distance

class Bus(Ticket):
    def fare(self):
        return self.distance * 5

class Train(Ticket):
    def fare(self):
        return self.distance * 3


t = Bus("A", "B", 100)
print("Fare:", t.fare())