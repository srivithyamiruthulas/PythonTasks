import random

class RandomPick:
    def __init__(self, data):
        self.data = data

    def pick(self):
        return random.choice(self.data)


data = [10, 20, 30, 40, 50]
r = RandomPick(data)
print("Random value:", r.pick())