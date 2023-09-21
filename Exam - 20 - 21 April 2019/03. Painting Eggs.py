#Read User Input
egg_size = input()
color = input()
amount = int(input())

total = 0

#Logic

if egg_size == "Large":
    if color == "Red":
        total = amount * 16
    elif color == "Green":
        total = amount * 12
    elif color == "Yellow":
        total = amount * 9
elif egg_size == "Medium":
    if color == "Red":
        total = amount * 13
    elif color == "Green":
        total = amount * 9
    elif color == "Yellow":
        total = amount * 7
if egg_size == "Small":
    if color == "Red":
        total = amount * 9
    elif color == "Green":
        total = amount * 8
    elif color == "Yellow":
        total = amount * 5

total *= 0.65

#Print Output

print(f"{total:.2f} leva.")