import sys

class ShowArguments:
    def display(self):
        return sys.argv
    
s = ShowArguments()
print("Arguments:", s.display())