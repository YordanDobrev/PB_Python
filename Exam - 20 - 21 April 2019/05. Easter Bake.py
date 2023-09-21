from math import ceil
#Read User Input
bread = int(input())

sugar = 0
wheat = 0
max_sugar = 0
max_wheat = 0

#Logic

for i in range(bread):
    current_sugar = int(input())
    current_wheat = int(input())

    sugar += current_sugar
    wheat += current_wheat

    if current_sugar > max_sugar:
        max_sugar = current_sugar

    if current_wheat > max_wheat:
        max_wheat = current_wheat

sugar_package = sugar / 950
wheat_package = wheat / 750

#Print Output

print(f"Sugar: {ceil(sugar_package)}")
print(f"Flour: {ceil(wheat_package)}")
print(f"Max used flour is {max_wheat} grams, max used sugar is {max_sugar} grams.")
