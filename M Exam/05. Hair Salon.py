#Read User Input
target = int(input())
command = input()
second_command = input()

money = 0

#Logic

while command != "closed":

    if command == "haircut":
        if second_command == "mens":
            money += 15
        elif second_command == "ladies":
            money += 20
        elif second_command == "kids":
            money += 10
    elif command == "color":
        if second_command == "touch up":
            money += 20
        elif second_command == "full color":
            money += 30

    if money >= target:
        break

    command = input()
    second_command = input()

#Print Output

if money >= target:
    print("You have reached your target for the day!")
else:
    difference = target - money
    print(f"Target not reached! You need {difference}lv. more.")

print(f"Earned money: {money}lv.")