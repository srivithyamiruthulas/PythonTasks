dict1={
    'Miruthula':[80,34,56,39,35,42,64],
    'Aathi':[80,95,62,34,59,39,64],
    'Lakshh':[34,56,39,73,56,39,81]
}
avg_dict={}

for name, marks in dict1.items():
    n=len(marks)
    summ=sum(marks)
    res=summ/n
    avg_dict[name]=round(res,2)

print("Student Average Marks:")
print(avg_dict)
    