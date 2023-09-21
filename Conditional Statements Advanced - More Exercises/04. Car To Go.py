#Read User Input
budget = float(input())
season = input()

#Logic
cabrio = 0
jeep = 0

if budget > 500:
    jeep = budget - (budget * 0.10)
    print("Luxury class")
    print(f"Jeep - {jeep:.2f}")
elif budget <= 100:
    print("Economy class")
    cabrio = budget - (budget * 0.65)
    jeep = budget - (budget * 0.35)

    if season == "Summer":
        print(f"Cabrio - {cabrio:.2f}")
    else:
        print(f"Jeep - {jeep:.2f}")

else:
    print("Compact class")
    cabrio = budget - (budget * 0.55)
    jeep = budget - (budget * 0.20)
    if season == "Summer":
        print(f"Cabrio - {cabrio:.2f}")
    else:
        print(f"Jeep - {jeep:.2f}")

#Print Output