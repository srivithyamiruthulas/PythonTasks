num1 = int(input())
num2 = int(input())
if num2 % 100 == 0 and num2 <= num1 and num1 - num2 >= 500:
    print("SUCCESS")
else:
    print("REJECTED")
