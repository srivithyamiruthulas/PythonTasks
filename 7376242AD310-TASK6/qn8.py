class Character:
    def attack(self):
        pass

class Warrior(Character):
    def attack(self):
        print("Warrior attacks with sword")

class Mage(Character):
    def attack(self):
        print("Mage attacks with magic")

c = Mage()
c.attack()