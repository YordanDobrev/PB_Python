#Read User Input
season = input()
kilometers = float(input())

total = 0

#Logic

if kilometers <= 5000:
    if season == "Spring" or season == "Autumn":
        total = (kilometers * 0.75) * 4
    elif season == "Summer":
        total = (kilometers * 0.9) * 4
    elif season == "Winter":
        total = (kilometers * 1.05) * 4
elif 5000 < kilometers <= 10000:
    if season == "Spring" or season == "Autumn":
        total = (kilometers * 0.95) * 4
    elif season == "Summer":
        total = (kilometers * 1.1) * 4
    elif season == "Winter":
        total = (kilometers * 1.25) * 4
elif kilometers > 10000:
    total = (kilometers * 1.45) * 4

total *= 0.90

#Print Output

print(f'{total:.2f}')