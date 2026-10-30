# A program that checks the largest number between 3 numbers
num1 = float(input("Enter num1: "))
num2 = float(input("Enter num2: "))
num3 = float(input("Enter num3: "))

if num1 >= num2 and num1 >= num3:
    print(f"The largest number is {num1}")
elif num2 >= num1 and num2 >= num3:
    print(f"{num2} is the largest")
else:
    print(f"{num3} is the largest")