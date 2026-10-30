#ELECTRICITY BILL CALCULATOR

#WRITE A PROGRAM THAT CALCULATES THE ELECTRICITY BILL BASED ON THE NUMBER OF UNITS CONSUMED. THE BILLING RATES ARE AS FOLLOWS:

#- For the first 100 units: 25 per unit

#- For the next 100 units (101-200): 35 per unit

#- For the next 100 units (201-300): 45 per unit

units = float(input("Enter the units: "))
if units < 0:
    print("Invalid Input")
elif units <= 100:
    bill = units * 25
elif units <= 200:
    bill = units * 35
elif units <= 300:
    bill = units * 45

print(f"The total bill is {bill}")
