num = int(input())
num1 = num
c = 0

while num1 != 0:
    c = c + 1
    num1 = num1 // 10

if c == 6 and num % 7 == 0:
    print("VALID")
else:
    print("INVALID")
