class Vehicle:
    def drive(self):
        pass

class AutoMode(Vehicle):
    def drive(self):
        print("Driving in autonomous mode")

class ManualMode(Vehicle):
    def drive(self):
        print("Driving in manual mode")


v = AutoMode()
v.drive()