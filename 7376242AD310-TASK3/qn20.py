s=input("Enter a string:")
res={"alphabets":0,"digits":0,"special":0}
for ch in s:
    if ch.isalpha():
        res["alphabets"]+=1
    elif ch.isdigit():
        res["digits"]+=1
    else:
        res["special"]+=1
print(res)
