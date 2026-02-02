num=int(input())
l=num%10
if num>=100000 and l%2==0:
    print("VALID")
else:
    print("INVALID")