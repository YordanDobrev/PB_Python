#Read User Input
flowers = input()
quantity = int(input())
budget = int(input())

price = 0

#Logic

if flowers == "Roses":
    price = 5
    if quantity > 80:
        price *= 0.9
elif flowers == "Dahlias":
    price = 3.8
    if quantity > 90:
        price *= 0.85
elif flowers == "Tulips":
    price = 2.80
    if quantity > 80:
        price *= 0.85
elif flowers == "Narcissus":
    price = 3
    if quantity < 120:
        price *= 1.15
elif flowers == "Gladiolus":
    price = 2.50
    if quantity < 80:
        price *= 1.20

total = quantity * price
difference = abs(total - budget)

#Print Output

if budget >= total:
    print(f"Hey, you have a great garden with {quantity} {flowers} and {difference:.2f} leva left.")
else:
    print(f"Not enough money, you need {difference:.2f} leva more.")