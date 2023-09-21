#Read User Input
budget = float(input())
season = input()

#Logic

alaska = 0
maroko = 0

if budget > 3000: #Hotel
    alaska = budget * 0.90
    maroko = budget * 0.90
    if season == "Summer":
        print(f"Alaska - Hotel - {alaska:.2f}")
    else:
        print(f"Morocco - Hotel - {maroko:.2f}")
elif budget <= 1000: #Camp
    alaska = budget * 0.65
    maroko = budget * 0.45
    if season == "Summer":
        print(f"Alaska - Camp - {alaska:.2f}")
    else:
        print(f"Morocco - Camp - {maroko:.2f}")
else: # Hut
    alaska = budget * 0.80
    maroko = budget * 0.60
    if season == "Summer":
        print(f"Alaska - Hut - {alaska:.2f}")
    else:
        print(f"Morocco - Hut - {maroko:.2f}")

#Print Output
