num = int(input())
c = 0
min1 = 999999

while c < num:
    num1 = int(input())
    if num1 < min1:
        min1 = num1
    c = c + 1
print(min1)
