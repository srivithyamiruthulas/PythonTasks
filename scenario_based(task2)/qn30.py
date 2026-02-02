num=int(input())
if num<10000:
    print(num*0.03/12)
elif num<=50000:
    print(num*0.05/12)
else:
    print(num*0.07/12)