#Read User Input
team = input()
matches = int(input())

#Logic

w_matches_counter = 0
d_matches_counter = 0
l_matches_counter = 0
points = 0

for i in range(matches):
    current_stage = input()
    if matches == 0:
        break
    if current_stage == "W":
        w_matches_counter += 1
        points += 3
    elif current_stage == "D":
        d_matches_counter += 1
        points += 1
    elif current_stage == "L":
        l_matches_counter += 1

#Print Output

if matches == 0:
    print(f"{team} hasn't played any games during this season.")
else:
    print(f"{team} has won {points} points during this season.")
    print("Total stats:")
    print(f"## W: {w_matches_counter}")
    print(f"## D: {d_matches_counter}")
    print(f"## L: {l_matches_counter}")
    print(f"Win rate: {(w_matches_counter / matches) * 100:.2f}%")