import os

class ListFiles:
    def show(self):
        return os.listdir()

l = ListFiles()
print("Files and Folders:", l.show())