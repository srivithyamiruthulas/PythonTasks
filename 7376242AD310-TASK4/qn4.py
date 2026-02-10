num=int(input("How many items are to be added? "))
dict1={}
def add_items(num):
    for i in range(num):
        item=input()
        quantity=input()
    
        dict1[item]=quantity
    return dict1
result=add_items(num)

print(f"Final Dictionary : {result}")
print("Do you want to contine adding? yes/No")

ans=input().lower()
if(ans=='yes'):
    print("How many items yet to be added? ")
    n=int(input())
    print(add_items(n))
else:
    pass

