class Reservation:
    def __init__(self, name):
        self.name = name

class Normal(Reservation):
    def confirm(self):
        print("Table reserved normally")

class VIP(Reservation):
    def confirm(self):
        print("VIP table reserved")


r = VIP("Sri")
r.confirm()