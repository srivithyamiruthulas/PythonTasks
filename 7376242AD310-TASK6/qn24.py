class Workout:
    def calories(self):
        pass

class Running(Workout):
    def calories(self):
        print("300 calories")

w = Running()
w.calories()