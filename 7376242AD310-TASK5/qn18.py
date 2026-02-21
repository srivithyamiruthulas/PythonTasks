class Patient:
    def __init__(self, name):
        self.name = name

class General(Patient):
    def cost(self):
        return 1000

class ICU(Patient):
    def cost(self):
        return 5000


p = ICU("Ravi")
print("Treatment Cost:", p.cost())