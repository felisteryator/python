#create a program that performs addition subtraction multiplication and division of two numbers based on user input.

#when declaring variable make sure you declare them as float to handle decimal numbers and operator as a variable ie. operator = input("Enter the operator (+, -, *, /): ")

num1 = float(input("Enter num1: "))
num2 = float(input("Enter num2: "))
operator = input("Enter operator(+, -, *, /): ")

if operator == "*":
    product  = num1 * num2
    print(f"The product of {num1} and {num2} is {product}")
elif operator == "+":
    sum  = num1 + num2
    print(f"The sum of {num1} and {num2} is {sum}")
elif operator == "-":
    difference  = num1 - num2
    print(f"The difference of {num1} and {num2} is {difference}")
elif operator == "/":
    if num2 != 0:
        quotient  = num1 / num2
        print(f"The quotient of {num1} and {num2} is {quotient}")
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operator")
    