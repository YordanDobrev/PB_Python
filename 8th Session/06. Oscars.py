#Read User Input
actor = input()
academy_points = float(input())
jury = int(input())

total_points = 0
temp = academy_points + total_points

#Logic

for i in range(jury):
    current_jury = len(input())
    jury_points = float(input())
    total_points += (current_jury * jury_points) / 2
    temp = academy_points + total_points
    if temp > 1250.5:
        break

#Print Output

if temp > 1250.5:
    print(f"Congratulations, {actor} got a nominee for leading role with {temp:.1f}!")
else:
    difference = 1250.5 - temp
    print(f"Sorry, {actor} you need {difference:.1f} more!")