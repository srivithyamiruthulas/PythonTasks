n = int(input("Enter the number:"))
num = n
summ = 0
while num != 0:
    digit = num % 10
    summ = summ + digit
    num = num // 10

if n % summ == 0:
    print("Harshad number")
else:
    print("Not a Harshad number")
