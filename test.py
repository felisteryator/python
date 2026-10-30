print("Program started")

try:
    number = int(input("Enter a number: "))
    print("Valid input:", number)
except ValueError:
    print("Invalid input! Please enter a number.")

print("Program finished")