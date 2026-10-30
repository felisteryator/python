def greet():
    print("This is my first function")
greet()

# Functions with parameters
def student(name, age, course):
    print(f"Student name is {name}")
    print(f"Student age is {age}")
    print(f"Student course is {course}")
student("Felister", 20, "Software engineering")
student("Charles", 21, "Commerce")

def add_number (a,b):
    return a + b
result = add_number(15,13)
print(f"The result is {result}")

def multiply_num (x,y):
    return x * y
product = multiply_num(21,3)
print(f"The product is {product}")