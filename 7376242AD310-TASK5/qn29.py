class Update:
    def apply(self):
        pass

class AutoUpdate(Update):
    def apply(self):
        print("Update applied automatically")

class ManualUpdate(Update):
    def apply(self):
        print("Update applied manually")


u = AutoUpdate()
u.apply()