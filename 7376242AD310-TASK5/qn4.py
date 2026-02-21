class Employee:
    def __init__(self, name, designation, basic_salary):
        self.name = name
        self.designation = designation
        self.basic_salary = basic_salary

    def calculate_salary(self):
        if self.designation == "Manager":
            return self.basic_salary + 5000
        elif self.designation == "Developer":
            return self.basic_salary + 3000
        else:
            return self.basic_salary + 1000


name = input("Enter name: ")
des = input("Enter designation: ")
salary = float(input("Enter basic salary: "))

emp = Employee(name, des, salary)
print("Final Salary:", emp.calculate_salary())