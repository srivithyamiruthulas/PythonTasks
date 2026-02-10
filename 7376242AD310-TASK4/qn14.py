passwords = ["Pass123!", "simple", "NoDigit!", "Only123"]
valid = []
invalid = []

for pwd in passwords:
    has_digit = any(char.isdigit() for char in pwd)
    has_special = any(not char.isalnum() for char in pwd)
    
    if has_digit and has_special:
        valid.append(pwd)
    else:
        invalid.append(pwd)

print(valid)
print(invalid)
