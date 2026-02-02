num=int(input())
num1=num
s=0
c=0
while num1!=0:
    r=num1%10
    s=s+r
    c=c+1
    num1=num1//10
if c==4 and s>15:
    print("ACCESSGRANTED")
else:
    print("ACCESSDENIED")