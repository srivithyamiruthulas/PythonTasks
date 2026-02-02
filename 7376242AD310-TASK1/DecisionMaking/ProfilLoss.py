cost=int(input("Enter the cost price:"))
sell=int(input("Enter the selling price:"))
if cost > 0 & sell > 0:
    if(cost-sell<0):
        print("Loss")
    elif(cost==sell):
        print("No profit no gain")
    else:
        print("Gain")
else:
    print("Invalid input")