num = int(input())
num1 = num
rev = 0

while num1 != 0:
    n = num1 % 10
    rev = rev * 10 + n
    num1 = num1 // 10

print(num + rev)