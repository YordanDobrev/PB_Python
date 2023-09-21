#Read User Input
month = input()
nights = int(input())

total_studio = 0
total_apartment = 0

#Logic
if month == "May" or month == "October":
    total_studio = 50
    total_apartment = 65
    if nights > 14:
        total_studio *= 0.70
        total_apartment *= 0.90
    elif nights > 7:
        total_studio *= 0.95
elif month == "June" or month == "September":
    total_studio = 75.20
    total_apartment = 68.70
    if nights > 14:
        total_studio *= 0.80
        total_apartment *= 0.90
elif month == "July" or month == "August":
    total_studio = 76
    total_apartment = 77
    if nights > 14:
        total_apartment *= 0.90

total_price_studio = total_studio * nights
total_price_apartment = total_apartment * nights

#Print Output

print(f"Apartment: {total_price_apartment:.2f} lv.")
print(f"Studio: {total_price_studio:.2f} lv.")
