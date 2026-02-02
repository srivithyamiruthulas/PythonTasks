num=int(input())
f=0
for i in range(3):
    num1=int(input())
    if num1==num:
        f=1
if f==1:
    print("ACCESSGRANTED")
else:
    print("CARDBLOCKED")
