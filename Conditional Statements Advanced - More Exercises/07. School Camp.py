#Read User Input
season = input()
group = input()
students = int(input())
nights = int(input())

total = 0

#Logic

if group == "boys" or group == "girls":
    if season == "Winter":
        total = students * 9.60
    elif season == "Spring":
        total = students * 7.20
    elif season == "Summer":
        total = students * 15
elif group == "mixed":
    if season == "Winter":
        total = students * 10
    elif season == "Spring":
        total = students * 9.50
    elif season == "Summer":
        total = students * 20

final_price = total * nights

if students >= 50:
    final_price *= 0.50
elif 50 > students >= 20:
    final_price *= 0.85
elif 20 > students >= 10:
    final_price *= 0.95

#Print Output

if season == "Winter" and group == "girls":
    print(f'Gymnastics {final_price:.2f} lv.')
elif season == "Winter" and group == "boys":
    print(f'Judo {final_price:.2f} lv.')
elif season == "Winter" and group == "mixed":
    print(f'Ski {final_price:.2f} lv.')

elif season == "Spring" and group == "girls":
    print(f'Athletics {final_price:.2f} lv.')
elif season == "Spring" and group == "boys":
    print(f'Tennis {final_price:.2f} lv.')
elif season == "Spring" and group == "mixed":
    print(f'Cycling {final_price:.2f} lv.')

elif season == "Summer" and group == "girls":
    print(f'Volleyball {final_price:.2f} lv.')
elif season == "Summer" and group == "boys":
    print(f'Football {final_price:.2f} lv.')
elif season == "Summer" and group == "mixed":
    print(f'Swimming {final_price:.2f} lv.')