num=int(input())
f=0
for i in range(num):
    num1=int(input())
    if num1>45:
        f=1
        break
if f==1:
    print("ALERT")
else:
    print("SAFE")