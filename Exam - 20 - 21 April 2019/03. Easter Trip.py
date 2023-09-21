#Read User Input
destination = input()
dates = input()
nights = int(input())

sum = 0

#Logic

if destination == "France":
    if dates == "21-23":
        sum += nights * 30
    elif dates == "24-27":
        sum += nights * 35
    elif dates == "28-31":
        sum += nights * 40
elif destination == "Italy":
    if dates == "21-23":
        sum += nights * 28
    elif dates == "24-27":
        sum += nights * 32
    elif dates == "28-31":
        sum += nights * 39
elif destination == "Germany":
    if dates == "21-23":
        sum += nights * 32
    elif dates == "24-27":
        sum += nights * 37
    elif dates == "28-31":
        sum += nights * 43

#Print Output

print(f"Easter trip to {destination} : {sum:.2f} leva.")