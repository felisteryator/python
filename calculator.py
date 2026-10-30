# create a complex calculator using inputoutput and control flows

print("Welcome to your calculator!")
while True:
    print("Choose an operation: ")
    print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Modulus\n6. Percentage\n7. Exponentiation\n8. Square root\n9. Exit")

    try:
        choice = int(input("Enter your choice: "))
        print("You entered:", choice)
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue
    try:
        if choice in (1,2,3,4,5):
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if choice == 1:
                print(f"The sum is {num1 + num2}")
            elif choice == 2:
                print(f"The difference is {num1 - num2}")
            elif choice == 3:
                print(f"The product is {num1 * num2}")
            elif choice == 4:
                if num2 == 0:
                    print("Cannot divide by zero")
                else:
                    print(f"The quotient is {num1 / num2}")
            elif choice == 5:
                if num2 == 0:
                    print("Cannot divide by zero")
                else:
                    print(f"The modulus is {num1 % num2}")
        elif choice == 6:
            num1 = float(input("Enter the total number: "))
            num2 = float(input("Enter the percentage to calculate: "))
            print(f"The percentage is {num2 / 100 * num1}")
        elif choice == 7:
            num1 = float(input("Enter the base number: "))
            num2 = float(input("Enter the exponent: "))
            print(f"The exponentiation is {num1 ** num2}")
        elif choice == 8:
            num = float(input("Enter the number: "))
            if num < 0:
                print("Cannot find the square root of a negative number")
            else:
                print(f"The square root is {num**0.5}")
        elif choice == 9:
            print("Thank you for using the calculator!")
            break
        else:
            print("Invalid Choice! Try again")
    except ValueError:
        print("Invalid input! Please enter valid numbers.")
