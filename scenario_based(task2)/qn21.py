num=float(input())
num1=float(input())
amt=num*num1
l=int(amt%10)

if l<=4:
    print(int(amt-l))
else:
    print(int(amt+(10-l)))
