num=int(input())
p=200

if num<5:
    print(0)
elif num<=12:
    print(p//2)
elif num<=59:
    print(p)
else:
    print(p-(p*30)//100)