num = int(input())
num1 = num
sum1 = 0

while num1 != 0:
    n = num1 % 10
    num1 = num1 // 10
    
    if n == 2 or n == 3 or n == 5 or n == 7:
        sum1 = sum1 + n

print(sum1)
