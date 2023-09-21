#Read User Input
target = float(input())

#Logic

sum = 0
target_reached = False
current_cocktail = input()

while current_cocktail != "Party!":
    drinks = int(input())
    last_order = len(current_cocktail) * drinks
    if last_order % 2 == 0:
        sum += len(current_cocktail) * drinks
    else:
        sum += (len(current_cocktail) * 0.75) * drinks

    if sum >= target:
        target_reached = True
        break

    current_cocktail = input()

#Print Output

if target_reached:
    print("Target acquired.")
    print(f"Club income - {sum:.2f} leva.")
else:
    difference = target - sum
    print(f"We need {difference:.2f} leva more.")
    print(f"Club income - {sum:.2f} leva.")