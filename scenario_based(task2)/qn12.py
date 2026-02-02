num = int(input())
c = 0

c = c + num // 500
num = num % 500

c = c + num // 200
num = num % 200

c = c + num // 100
num = num % 100

c = c + num // 50
num = num % 50

c = c + num // 20
num = num % 20

c = c + num // 10
num = num % 10
c = c + num
print(c)