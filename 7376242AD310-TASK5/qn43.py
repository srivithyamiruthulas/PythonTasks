import os

class CreateDirectory:
    def __init__(self, name):
        self.name = name

    def create(self):
        os.mkdir(self.name)
        return "Directory created"


name = input("Enter folder name: ")
c = CreateDirectory(name)
print(c.create())