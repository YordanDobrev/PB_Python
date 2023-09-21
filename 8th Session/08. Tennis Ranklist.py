#Read User Input
tournaments = int(input())
rang_list_points = int(input())

points = 0
tournaments_won = 0

#Logic

for i in range(tournaments):
    current_stage = input()

    if current_stage == "W":
        points += 2000
        tournaments_won += 1
    elif current_stage == "F":
        points += 1200
    elif current_stage == "SF":
        points += 720

total = points + rang_list_points
average_points = int(points / tournaments)
percentage_tournamets_won = (tournaments_won / tournaments) * 100

#Print Output

print(f"Final points: {total}")
print(f"Average points: {average_points}")
print(f"{percentage_tournamets_won:.2f}%")