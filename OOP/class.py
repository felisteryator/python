class Student:
    #constructor
    def __init__(self,name,age):
        self.name = name
        self.age = age

#object
student1 = Student("Felister", 20)

print(f"Student name: {student1.name}")

class Car:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year

car1 = Car("Mazda", "cx5", 2020)

print(f"Car brand: {car1.brand}")
print(f"Car model: {car1.model}")
print(f"Car year: {car1.year}")
        