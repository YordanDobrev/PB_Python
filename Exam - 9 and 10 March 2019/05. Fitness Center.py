#Read User Input
visitors = int(input())

#Logic

back = 0
chest = 0
legs = 0
abs = 0
protein_shake = 0
protein_bar = 0

for i in range(visitors):
    command = input()

    if command == "Back":
        back += 1
    elif command == "Chest":
        chest += 1
    elif command == "Legs":
        legs += 1
    elif command == "Abs":
        abs += 1
    elif command == "Protein shake":
        protein_shake += 1
    elif command == "Protein bar":
        protein_bar += 1

work_out = ((back + chest + legs + abs) / visitors) * 100
protein = ((protein_shake + protein_bar) / visitors) * 100

#Print Output

print(f"{back} - back")
print(f"{chest} - chest")
print(f"{legs} - legs")
print(f"{abs} - abs")
print(f"{protein_shake} - protein shake")
print(f"{protein_bar} - protein bar")
print(f"{work_out:.2f}% - work out")
print(f"{protein:.2f}% - protein")