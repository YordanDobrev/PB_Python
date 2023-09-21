#Read User Input
actor = input()
starting_points = float(input())
jury = int(input())

total_points = starting_points
oscar_won = False

#Logic

for oscar in range(jury):
    current_jury = input()
    current_jury_points = float(input())

    total_points += (len(current_jury) * current_jury_points) / 2

    if total_points >= 1250.50:
        oscar_won = True
        break

#Print Output

if oscar_won:
    print(f"Congratulations, {actor} got a nominee for leading role with {total_points:.1f}!")
else:
    difference = 1250.50 - total_points
    print(f"Sorry, {actor} you need {difference:.1f} more!")