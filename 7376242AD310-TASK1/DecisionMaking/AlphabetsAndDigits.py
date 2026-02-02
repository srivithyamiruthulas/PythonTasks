input=input("Enter a word:")
if input.isdigit():
    print("Digit")
elif( input.isalpha):
    print("Alphabets")
else:
    print("Special Characters!")