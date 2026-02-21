class Ride:
    def __init__(self, distance):
        self.distance = distance

class Mini(Ride):
    def fare(self):
        return self.distance * 8

class Prime(Ride):
    def fare(self):
        return self.distance * 12


r = Prime(10)
print("Fare:", r.fare())