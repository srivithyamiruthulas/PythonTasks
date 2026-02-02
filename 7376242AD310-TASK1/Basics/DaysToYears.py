Total_days=int(input("Enter the tottal number of days:"))
leapyrs=input("Is there a leap year included? (yes/no): ")
if leapyrs.lower()=='yes':
    years=(Total_days-1)//365
else:
    years=Total_days//365
months=(Total_days-years*365)//30
days=(Total_days-years*365)%30

print(f"{Total_days} days is approximately {years} years, {months} months and {days} days")