# Can allow duplicates
# Ordered, changeable

myproducts = ["bread", "Milk", "Sugar", "Blueband", "sugar"]

myproducts[1] = "honey"
print(f"I like drinking tea that has {myproducts[1]}")
print(myproducts)
for i in myproducts:
    print(f"{i}")
print(f"I have {len(myproducts)} products")
print(type(myproducts))

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
    list1.append(x)
print(list1)

myfruits = ["mangoes", "apples", "bananas", "oranges"]

for m in myfruits:
    print(f"I have {m}")

# Imagine you are building a school that calculates the average marks

marks = [65,89,64,85,90]

total = 0
for n in marks:
    total += n
average = total / len(marks)
print(f"Total marks: {total}")
print(f"Average marks: {average}")