input=int(input("enter your mark:"))
if((input>0) & (input<100)):
    if(input>90):
        print("Grade A")
    elif(input>85):
        print("Grade B")
    elif(input>65):
        print("Grade C")
    else:
        print("Grage D")
else:
    print("Invalid input")