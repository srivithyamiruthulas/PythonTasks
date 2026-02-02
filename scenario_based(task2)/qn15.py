num = int(input())
if num < 1000:
    print(num)
elif num < 3000:
    print(num - (num * 10) // 100)
elif num < 5000:
    print(num - (num * 20) // 100)
else:
    print(num - (num * 30) // 100)