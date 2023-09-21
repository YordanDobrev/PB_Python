#Read User Input
team = input()
souvenir = input()
souvenir_quantity = int(input())

total = 0
correct_data = False
correct_data_country = False
#Logic

if team == "Argentina":
    if souvenir == "flags":
        total = souvenir_quantity * 3.25
    elif souvenir == "caps":
        total = souvenir_quantity * 7.20
    elif souvenir == "posters":
        total = souvenir_quantity * 5.10
    elif souvenir == "stickers":
        total = souvenir_quantity * 1.25
    else:
        correct_data = True
        print(f"Invalid stock!")
elif team == "Brazil":
    if souvenir == "flags":
        total = souvenir_quantity * 4.20
    elif souvenir == "caps":
        total = souvenir_quantity * 8.50
    elif souvenir == "posters":
        total = souvenir_quantity * 5.35
    elif souvenir == "stickers":
        total = souvenir_quantity * 1.20
    else:
        correct_data = True
        print(f"Invalid stock!")
elif team == "Croatia":
    if souvenir == "flags":
        total = souvenir_quantity * 2.75
    elif souvenir == "caps":
        total = souvenir_quantity * 6.90
    elif souvenir == "posters":
        total = souvenir_quantity * 4.95
    elif souvenir == "stickers":
        total = souvenir_quantity * 1.10
    else:
        correct_data = True
        print(f"Invalid stock!")
elif team == "Denmark":
    if souvenir == "flags":
        total = souvenir_quantity * 3.10
    elif souvenir == "caps":
        total = souvenir_quantity * 6.50
    elif souvenir == "posters":
        total = souvenir_quantity * 4.80
    elif souvenir == "stickers":
        total = souvenir_quantity * 0.90
    else:
        correct_data = True
        print(f"Invalid stock!")
else:
    correct_data_country = True
    print(f"Invalid country!")

#Print Output

if not correct_data and not correct_data_country:
    print(f"Pepi bought {souvenir_quantity} {souvenir} of {team} for {total:.2f} lv.")