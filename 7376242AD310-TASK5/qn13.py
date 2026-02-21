class Exam:
    def __init__(self, subject, max_marks):
        self.subject = subject
        self.max_marks = max_marks

class Internal(Exam):
    def evaluate(self, marks):
        return "Pass" if marks >= 40 else "Fail"

class External(Exam):
    def evaluate(self, marks):
        return "Pass" if marks >= 50 else "Fail"


e = Internal("Math", 100)
print(e.evaluate(45))