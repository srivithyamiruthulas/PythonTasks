class Bot:
    def respond(self):
        pass

class FriendlyBot(Bot):
    def respond(self):
        print("Hello!")

b = FriendlyBot()
b.respond()