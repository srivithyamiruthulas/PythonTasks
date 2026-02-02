num=int(input())
num1=int(input())
i=0
while i<num1:
    if num>0:
        print("BOOKED")
        num=num-1
    else:
        print("HOUSEFULL")
        break
    i=i+1
if num>0:
    print(num)