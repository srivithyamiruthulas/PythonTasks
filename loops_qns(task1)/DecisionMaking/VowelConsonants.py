input=input("Enter a character:")
if (len(input)==1):
    if input.lower in ['a','e','i','o','u']:
        print("Vowel!")
    else:
        print("Consonant!")
else:
    print("Please enter a character for input!")