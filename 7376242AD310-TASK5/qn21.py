class Plan:
    def __init__(self, user):
        self.user = user

class Basic(Plan):
    def bill(self):
        return 199

class Premium(Plan):
    def bill(self):
        return 499


p = Premium("Sri")
print("Bill Amount:", p.bill())