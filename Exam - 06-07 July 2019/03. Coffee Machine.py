#Read User Input
coffee = input()
sugar = input()
drinks = int(input())

#Logic

sum = 0

if coffee == "Espresso":
    if sugar == "Without":
        sum = (drinks * 0.9) * 0.65
    elif sugar == "Normal":
        sum = drinks
    elif sugar == "Extra":
        sum = drinks * 1.2
elif coffee == "Cappuccino":
    if sugar == "Without":
        sum = drinks * 0.65
    elif sugar == "Normal":
        sum = drinks * 1.2
    elif sugar == "Extra":
        sum = drinks * 1.6
elif coffee == "Tea":
    if sugar == "Without":
        sum = (drinks * 0.5) * 0.65
    elif sugar == "Normal":
        sum = drinks * 0.6
    elif sugar == "Extra":
        sum = drinks * 0.7

if coffee == "Espresso" and drinks > 5:
    sum *= 0.75

if sum > 15:
    sum *= 0.80

#Print Output

print(f"You bought {drinks} cups of {coffee} for {sum:.2f} lv.")