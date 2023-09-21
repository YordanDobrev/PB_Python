from math import floor

#Read User Input
tournaments = int(input())
starting_points = int(input())

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

average_points = floor(points / tournaments)
average_won = (tournaments_won / tournaments) * 100
final_points = starting_points + points

#Print Output

print(f"Final points: {final_points}")
print(f"Average points: {average_points}")
print(f"{average_won:.2f}%")