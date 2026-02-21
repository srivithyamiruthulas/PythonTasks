class Grading:
    def evaluate(self):
        pass

class Internal(Grading):
    def evaluate(self):
        print("Grade A")

g = Internal()
g.evaluate()