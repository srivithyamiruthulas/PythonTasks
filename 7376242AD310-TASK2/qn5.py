num = int(input())
num1 = num
c = 0
o = 0

while num1 != 0:
    n = num1 % 10
    num1 = num1 // 10
    if n % 2 == 0:
        c = c + 1
    else:
        o = o + 1
print(c, o)
