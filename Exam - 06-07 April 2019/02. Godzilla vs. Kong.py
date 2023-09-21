#Read User Input
budget = float(input())
staists = int(input())
clothes_price = float(input())

#Logic

decor = budget * 0.1

if staists > 150:
    clothes_price *= 0.9

sum = (staists * clothes_price) + decor

#Print Output

if sum > budget:
    difference = sum - budget
    print("Not enough money!")
    print(f"Wingard needs {difference:.2f} leva more.")
else:
    difference = budget - sum
    print("Action!")
    print(f"Wingard starts filming with {difference:.2f} leva left.")