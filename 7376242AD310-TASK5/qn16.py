class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

class GradeA(Student):
    def grade(self):
        return "A" if self.marks >= 80 else "B"


s = GradeA("Sri", 85)
print("Grade:", s.grade())