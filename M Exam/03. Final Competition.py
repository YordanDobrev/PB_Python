#Read User Input
dancers = int(input())
points = float(input())
season = input()
destination = input()

#Logic

total = 0

if destination == "Bulgaria":
    if season == "summer":
        total = (points * dancers) * 0.95
    elif season == "winter":
        total = (points * dancers) * 0.92
elif destination == "Abroad":
    if season == "summer":
        total = (points * dancers) * 0.90
    elif season == "winter":
        total = (points * dancers) * 0.85

if destination == "Abroad":
    total += total * 0.5

final = total * 0.75
money_per_dancer = (total-final) / dancers

#Print Output

print(f"Charity - {final:.2f}")
print(f"Money per dancer - {money_per_dancer:.2f}")