import sys

class FirstArgument:
    def show(self):
        if len(sys.argv) > 1:
            return sys.argv[1]
        else:
            return "No argument provided"


f = FirstArgument()
print("First Argument:", f.show())