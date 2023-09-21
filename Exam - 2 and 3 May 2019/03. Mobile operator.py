#Read User Input
contract = input()
type = input()
internet = input()
months = int(input())

#Logic

total = 0

if contract == "one":
    if type == "Small":
        total = 9.98
        if internet == "yes":
            if total < 10:
                total += 5.50
            elif total <= 30:
                total += 4.35
            elif total > 30:
                total += 3.85
    elif type == "Middle":
        total = 18.99
        if internet == "yes":
            if total < 10:
                total += 5.50
            elif total <= 30:
                total += 4.35
            elif total > 30:
                total += 3.85
    elif type == "Large":
        total = 25.98
        if internet == "yes":
            if total < 10:
                total += 5.50
            elif total <= 30:
                total += 4.35
            elif total > 30:
                total += 3.85
    elif type == "ExtraLarge":
        total = 35.99
        if internet == "yes":
            if total < 10:
                total += 5.50
            elif total <= 30:
                total += 4.35
            elif total > 30:
                total += 3.85

elif contract == "two":
    if type == "Small":
        total = 8.58
        if internet == "yes":
            if total < 10:
                total += 5.50
            elif total <= 30:
                total += 4.35
            elif total > 30:
                total += 3.85
    elif type == "Middle":
        total = 17.09
        if internet == "yes":
            if total < 10:
                total += 5.50
            elif total <= 30:
                total += 4.35
            elif total > 30:
                total += 3.85
    elif type == "Large":
        total = 23.59
        if internet == "yes":
            if total < 10:
                total += 5.50
            elif total <= 30:
                total += 4.35
            elif total > 30:
                total += 3.85
    elif type == "ExtraLarge":
        total = 31.79
        if internet == "yes":
            if total < 10:
                total += 5.50
            elif total <= 30:
                total += 4.35
            elif total > 30:
                total += 3.85

total *= months

#Print Output

if contract == "two":
    total *= 0.9625
    print(f"{total:.2f} lv.")
else:
    print(f"{total:.2f} lv.")