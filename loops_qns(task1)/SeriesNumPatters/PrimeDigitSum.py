n = int(input("Enter the number:"))
num = n
sum = 0
while num != 0:
    digit = num % 10
    if digit == 2 or digit == 3 or digit == 5 or digit == 7:
        sum = sum + digit
    num = num // 10
print("Sum of prime digits:", sum)