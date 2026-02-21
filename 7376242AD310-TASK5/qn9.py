class Course:
    def __init__(self, name):
        self.name = name
        self.students = []

    def register(self, student):
        if student not in self.students:
            self.students.append(student)
            print("Registered successfully")
        else:
            print("Already registered")


c = Course("AI")
c.register("Sri")
c.register("Sri")