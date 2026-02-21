class Enemy:
    def act(self):
        pass

class Zombie(Enemy):
    def act(self):
        print("Zombie attacks")

z = Zombie()
z.act()