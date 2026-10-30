from abc import ABC, abstractmethod

class HospitalService(ABC):
    # Abstraction

    @abstractmethod
    def process_payment(self, amount):
        pass

class Patient(HospitalService):
    def __init__(self, full_name, ID, phone_number, age, Acc_balance):
        # Instance attributes
        self.full_name = full_name
        self.ID = ID
        self.phone_number = phone_number
        self.age = age
# Private-like attribute
        self.__Acc_balance = Acc_balance

    def check_balance(self):
        return self.__Acc_balance

    def deposit(self, amount):
        if amount > 0:
            self.__Acc_balance += amount
            print("Deposit successfull")

        else:
            print("Invalid Amount!")

    def withdraw(self, amount):
        if self.__Acc_balance >= amount:
            self.__Acc_balance -= amount
            print("Withdrawal successful")

        elif amount > self.__Acc_balance:
            print("Invalid Amount")

        else:
            print("Insufficient funds")

class Doctor:
    def __init__(self, name, ID, specialization, consultation_fee):
        self.name = name
        self.ID = ID
        self.specialization = specialization
        self.consultation_fee = consultation_fee

class Outpatient(Patient):
    def patient_type():
        print("Outpatient Patient")

    def process_payment(self, amount):
        total = amount + 100

        if self.__Acc_balance >= total:
            print(f"Payment successful! Amount Paid is: {total}")
        else:
            print("Unable to pay! Insufficient funds")


class Inpatient(Patient):
    def patient_type():
        print("Inpatient Patient")

    def process_payment(self, amount):
            total = amount + 200
    
            if self.__Acc_balance >= total:
                print(f"Payment successful! Amount Paid is: {total}")
            else:
                print("Unable to pay! Insufficient funds")