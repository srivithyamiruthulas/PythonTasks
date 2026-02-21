import sys

class CheckArguments:
    def validate(self):
        if len(sys.argv) <= 1:
            print("No arguments provided")
            sys.exit()
        else:
            print("Arguments exist")


c = CheckArguments()
c.validate()