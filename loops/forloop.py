# for loop

for i in range(1,11):
    print(f"Welcome to my shop! Customer {i}")

customers = ["Erick", "Angel", "Cynthia", "Joel", "Linet"]

for c in customers:
     print(f"Welcome to today's class! {c}")

# calculate expense for what you bought
# bread ksh 90
# milk ksh 120
# sugar ksh 160

my_shopping = [90, 120, 160]
total = 0
for m in my_shopping:
    total = total + m
print(f"My total shopping cost is {total}")

total = 0
for num in range(1,6):
    total = total + 100
print(f"Total money collected : Ksh {total}")

# imagine you have five custtomers, and each pay you 100.
# create a script to get the total
