num = int(input())
d=0

while d<=9:
    num1=num
    f=0
    while num1!= 0:
        n=num1%10
        if n==d:
            f=1
            break
        num1=num1//10
    if f==0:
        print(d)
        break
    d=d+1
