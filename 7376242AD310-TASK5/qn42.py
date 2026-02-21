import os

class CheckDirectory:
    def __init__(self, path):
        self.path = path

    def check(self):
        if os.path.exists(self.path):
            return "Directory exists"
        else:
            return "Directory does not exist"


path = input("Enter directory path: ")
d = CheckDirectory(path)
print(d.check())