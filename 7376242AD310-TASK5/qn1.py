class student:
    def __init__(self,name,dept,year,cgpa):
        self.name=name
        self.year=year
        self.cgpa=cgpa
        self.dept=dept
    def is_eligible(self):
        if(self.cgpa>7.5 and self.year>=3):
            return "Eligible for placements"
        else:
            return "Not eligible for placements"
name=input("Enter name: ")
year=int(input("Enter year in numbers: "))
cgpa=float(input("Enter your CGPA: "))
dept=input("Enter your dept:")

stud1=student(name,dept,year,cgpa)
print(stud1.is_eligible())