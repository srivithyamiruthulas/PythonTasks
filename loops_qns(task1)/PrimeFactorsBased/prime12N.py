n=int(input("Enter a number:"))
def prime(n):
    c=0
    for i in range(2,n):
        if (n%i==0):
            c+=1
    if(c==0):
        return 1   
    else:
        return 0
summ=0

for j in range(n+1):
    if prime(j):
        print(j)
        summ+=j
    else:
        pass
print(f"The sum of all Prime numbers between 1 to N is {summ}")
