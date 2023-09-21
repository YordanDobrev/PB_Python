#Read User Input
budget = int(input())
season = input()
fisherman = int(input())

price = 0

#Logic
if season == "Spring":
    price = 3000
elif season == "Summer" or season == "Autumn":
    price = 4200
elif season == "Winter":
    price = 2600

if fisherman <= 6:
    price *= 0.9
elif fisherman > 11:
    price *= 0.75
else:
    price *= 0.85

if fisherman % 2 == 0 and season != "Autumn":
    price *= 0.95

difference = abs(budget-price)

#Print Output

if budget >= price:
    print(f"Yes! You have {difference:.2f} leva left.")
else:
    print(f"Not enough money! You need {difference:.2f} leva.")