# Read User Input
trunk = float(input())
command = input()

# Logic

volume = 0
suitcases = 0

while command != "End":
    current_space = float(command)
    if current_space > trunk:
        break

    if volume == 3:
        trunk -= current_space * 1.10
        volume = 0
    else:
        trunk -= current_space

    volume += 1
    suitcases += 1
    command = input()

# Print Output

if command == "End":
    print(f"Congratulations! All suitcases are loaded!")
else:
    print(f"No more space!")

print(f"Statistic: {suitcases} suitcases loaded.")