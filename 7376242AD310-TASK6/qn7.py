class Employee:
    def __init__(self, salary):
        self.__salary = salary

    def update_salary(self, salary):
        self.__salary = salary

    def show_salary(self):
        print("Salary:", self.__salary)

e = Employee(30000)
e.update_salary(40000)
e.show_salary()