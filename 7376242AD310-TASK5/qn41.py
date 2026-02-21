import os

class CurrentDirectory:
    def show(self):
        return os.getcwd()


c = CurrentDirectory()
print("Current Directory:", c.show())