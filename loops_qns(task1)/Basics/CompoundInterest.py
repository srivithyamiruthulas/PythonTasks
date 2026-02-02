P=int(input("Enter the Principal amount:"))
R=float(input("Enter the Rate of interest:"))
T=int(input("Enter the Time period in years:"))
CI=P*(1+R/100)**T - P
print("The Compound Interest is:", CI)
