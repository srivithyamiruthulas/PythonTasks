a=int(input("enter a:"))
b=int(input("enter b:"))
sum=a+b
mul=a*b
if(sum>mul):
    print("Greater")
elif(sum==mul):
    print("Equal")
else:
    print("Lesser")