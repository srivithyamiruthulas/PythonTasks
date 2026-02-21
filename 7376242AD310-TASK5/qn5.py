class Vehicle:
    def __init__(self, brand, fuel):
        self.brand = brand
        self.fuel = fuel

class Car(Vehicle):
    def drive(self):
        print(self.brand, "car is driving smoothly")

class Bike(Vehicle):
    def drive(self):
        print(self.brand, "bike is zooming fast")


car = Car("Toyota", "Petrol")
bike = Bike("Yamaha", "Petrol")

car.drive()
bike.drive()