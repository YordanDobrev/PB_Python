#Read User Input
player_one = input()
player_two = input()
command = input()

p_1_points = 0
p_2_points = 0

total_points = 0

#Logic

while command != "End of game":
    command = int(command)
    command_2 = int(input())

    if command > command_2:
        p_1_points += command - command_2
    elif command < command_2:
        p_2_points += command_2 - command
    else:
        print(f"Number wars!")
        if p_1_points > p_2_points:
            print(f"{player_one} is winner with {p_1_points} points")
        else:
            print(f"{player_two} is winner with {p_2_points} points")
        break
    total_points += command + command_2
    command = input()

#Print Output

if command == "End of game":
    print(f"{player_one} has {p_1_points} points")
    print(f"{player_two} has {p_2_points} points")