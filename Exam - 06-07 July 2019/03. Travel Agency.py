#Read User Input
city = input()
package = input()
vip = input()
days = int(input())

correct_days_data = False
correct_data = False
#Logic

sum = 0

if days <= 0:
    correct_days_data = True
elif days >= 7:
    days -= 1

if city == "Bansko" or city == "Borovets":
    if package == "withEquipment":
        if vip == "yes":
            sum = (days * 100) * 0.9
        elif vip == "no":
            sum = days * 100
    elif package == "noEquipment":
        if vip == "yes":
            sum = (days * 80) * 0.95
        elif vip == "no":
            sum = days * 80

elif city == "Varna" or city == "Burgas":
    if package == "withBreakfast":
        if vip == "yes":
            sum = (days * 130) * 0.88
        elif vip == "no":
            sum = days * 130
    elif package == "noBreakfast":
        if vip == "yes":
            sum = (days * 100) * 0.93
        elif vip == "no":
            sum = days * 100
else:
    correct_data = True

#Print Output

if correct_days_data:
    print("Days must be positive number!")
elif correct_data:
    print("Invalid input!")
else:
    print(f"The price is {sum:.2f}lv! Have a nice time!")
