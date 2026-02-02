n=int(input("Enter number: "))
largest=-1
second=-1
while n>0:
    d = n%10
    if d>largest:
        second=largest
        largest=d
    elif d!=largest and d>second:
        second = d
    n//=10
if second==-1:
    print(-1)
else:
    print("Second largest digit:",second)
