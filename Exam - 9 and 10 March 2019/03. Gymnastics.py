#Read User Input
country = input()
gymnastic = input()

total = 0

#Logic

if country == "Russia":
    if gymnastic == "ribbon":
        total = 9.1 + 9.4
    elif gymnastic == "hoop":
        total = 9.3 + 9.8
    elif gymnastic == "rope":
        total = 9.6 + 9
elif country == "Bulgaria":
    if gymnastic == "ribbon":
        total = 9.6 + 9.4
    elif gymnastic == "hoop":
        total = 9.55 + 9.75
    elif gymnastic == "rope":
        total = 9.5 + 9.4
elif country == "Italy":
    if gymnastic == "ribbon":
        total = 9.2 + 9.5
    elif gymnastic == "hoop":
        total = 9.45 + 9.35
    elif gymnastic == "rope":
        total = 9.7 + 9.15

target = ((20 - total) / 20) * 100

#Print Output

print(f"The team of {country} get {total:.3f} on {gymnastic}.")
print(f"{target:.2f}%")