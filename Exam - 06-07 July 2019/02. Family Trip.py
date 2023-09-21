#Read User Input
budget = float(input())
nights = int(input())
price_per_night = float(input())
extra_spent = int(input()) / 100

#Logic

total = 0
if nights > 7:
    total = nights * (price_per_night * 0.95) + (budget * extra_spent)
else:
    total = nights * price_per_night + (budget * extra_spent)

difference = abs(budget - total)

#Print Output

if budget >= total:
    print(f"Ivanovi will be left with {difference:.2f} leva after vacation.")
else:
    print(f"{difference:.2f} leva needed.")