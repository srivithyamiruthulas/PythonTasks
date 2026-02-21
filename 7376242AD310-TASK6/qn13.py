class Vehicle:
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started")

v = Car()
v.start_engine()