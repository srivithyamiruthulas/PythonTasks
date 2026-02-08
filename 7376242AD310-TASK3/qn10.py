names = ['Anand', 'Yoga', 'Hema', 'Miruthula', 'Selvarani', 'Siva', 'Hari']
marks = [91, 90, 80, 100, 90, 80, 95]
topper=dict(sorted(zip(names,marks),key=lambda x: x[1],reverse=True))
#print(f"The student list mapped with marks is:\n {combined}\n")
print(f"The Top rank student: {topper}")