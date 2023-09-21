#Read User Input
games = int(input())

hearthstone = 0
fornite = 0
overwatch = 0
others = 0

#Logic

for i in range(games):
    current_came = input()

    if current_came == "Hearthstone":
        hearthstone += 1
    elif current_came == "Fornite":
        fornite += 1
    elif current_came == "Overwatch":
        overwatch += 1
    else:
        others += 1

#Print Output

print(f"Hearthstone - {(hearthstone / games) * 100:.2f}%")
print(f"Fornite - {(fornite / games) * 100:.2f}%")
print(f"Overwatch - {(overwatch / games) * 100:.2f}%")
print(f"Others - {(others / games) * 100:.2f}%")