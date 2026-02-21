class Person:
    def show_role(self):
        pass

class Student(Person):
    def show_role(self):
        print("I am a Student")

class Teacher(Person):
    def show_role(self):
        print("I am a Teacher")

p = Student()
p.show_role()