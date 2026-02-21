class Employee:
    def calculate_salary(self):
        pass

class FullTime(Employee):
    def calculate_salary(self):
        print(50000)

e = FullTime()
e.calculate_salary()