import random

class ShuffleList:
    def __init__(self, data):
        self.data = data

    def shuffle(self):
        random.shuffle(self.data)
        return self.data


data = [1, 2, 3, 4, 5]
s = ShuffleList(data)
print("Shuffled list:", s.shuffle())