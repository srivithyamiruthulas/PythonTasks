class Package:
    def __init__(self, sender, receiver):
        self.sender = sender
        self.receiver = receiver
        self.status = "Shipped"

class Express(Package):
    def update_status(self):
        self.status = "Delivered in 1 day"

class Standard(Package):
    def update_status(self):
        self.status = "Delivered in 5 days"


pkg = Express("A", "B")
pkg.update_status()
print(pkg.status)