class Character:
    def __init__(self, health, power):
        self.health = health
        self.power = power

class Warrior(Character):
    def attack(self):
        print("Warrior attacks with sword!")

class Mage(Character):
    def attack(self):
        print("Mage attacks with magic!")


c = Warrior(100, 50)
c.attack()