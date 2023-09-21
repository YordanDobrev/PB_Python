#Read User Input
drink = input()
city = input()
quantity = float(input())

total = 0

#Logic
if city == "Sofia":
    if drink == "coffee":
        total = quantity * 0.5
    elif drink == "water":
        total = quantity * 0.8
    elif drink == "beer":
        total = quantity * 1.2
    elif drink == "sweets":
        total = quantity * 1.45
    elif drink == "peanuts":
        total = quantity * 1.60

elif city == "Plovdiv":
    if drink == "coffee":
        total = quantity * 0.4
    elif drink == "water":
        total = quantity * 0.7
    elif drink == "beer":
        total = quantity * 1.15
    elif drink == "sweets":
        total = quantity * 1.30
    elif drink == "peanuts":
        total = quantity * 1.50

elif city == "Varna":
    if drink == "coffee":
        total = quantity * 0.45
    elif drink == "water":
        total = quantity * 0.7
    elif drink == "beer":
        total = quantity * 1.1
    elif drink == "sweets":
        total = quantity * 1.35
    elif drink == "peanuts":
        total = quantity * 1.55

#Print Output

print(total)