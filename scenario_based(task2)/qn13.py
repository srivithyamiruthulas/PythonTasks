num = int(input())
num1 = num
sum1 = 0

while num1 != 0:
    n = num1 % 10
    f = 1
    i = 1
    
    while i <= n:
        f = f * i
        i = i + 1
    
    sum1 = sum1 + f
    num1 = num1 // 10

if sum1 == num:
    print("STRONG")
else:
    print("NOT STRONG")
