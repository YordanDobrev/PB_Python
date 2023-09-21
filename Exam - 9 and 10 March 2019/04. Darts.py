#Read User Input
player = input()
strike = input()


#Logic

current_points = 301
shots = 0
missed = 0

while strike != "Retire":
    score = int(input())
    if strike == "Single":
        if score > current_points:
            strike = input()
            missed += 1
            continue
        current_points -= score
        shots += 1

    elif strike == "Double":
        if score * 2 > current_points:
            strike = input()
            missed += 1
            continue
        current_points -= score * 2
        shots += 1
    elif strike == "Triple":
        if score * 3 > current_points:
            strike = input()
            missed += 1
            continue
        current_points -= score * 3
        shots += 1

    if current_points == 0:
        break
    strike = input()

#Print Output
if strike == "Retire":
    print(f"{player} retired after {missed} unsuccessful shots.")
else:
    print(f"{player} won the leg with {shots} shots.")
