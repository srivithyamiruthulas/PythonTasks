import random

class RandomSample:
    def __init__(self, data):
        self.data = data

    def sample(self, count):
        return random.sample(self.data, count)


data = [1, 2, 3, 4, 5, 6, 7]
rs = RandomSample(data)
print("Random samples:", rs.sample(3))