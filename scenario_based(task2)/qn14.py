num = int(input())
c = 0
i = 2

while i <= num:
    n = 2
    f = 0
    while n <= i // 2:
        if i % n == 0:
            f = 1
            break
        n = n + 1
    if i > 1 and f == 0:
        c = c + 1
    i = i + 1

print(c)
