#Read User Input
budget = float(input())
season = input()

place = "Europe"
accommodation = "Hotel"
total = 0

#Logic
if budget <= 100:
    place = "Bulgaria"
    if season == "summer":
        accommodation = "Camp"
        total = budget * 0.30
    elif season == "winter":
        total = budget * 0.70

elif budget <= 1000:
    place = "Balkans"
    if season == "summer":
        accommodation = "Camp"
        total = budget * 0.40
    elif season == "winter":
        total = budget * 0.80

else:
    place = "Europe"
    total = budget * 0.90

#Print Output

print(f"Somewhere in {place}")
print(f"{accommodation} - {total:.2f}")