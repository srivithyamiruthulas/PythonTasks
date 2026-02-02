a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
x, y = a, b
while y != 0:
    x, y = y, x % y
gcd = x
lcm = (a * b) // gcd
print("LCM is:", lcm)