#Read User Input


#Logic

won = 0
lost = 0
draw = 0

for i in range(3):
    match = input()
    if int(match[0]) > int(match[2]):
        won += 1
    elif int(match[0]) < int(match[2]):
        lost += 1
    elif int(match[0]) == int(match[2]):
        draw += 1

#Print Output

print(f"Team won {won} games.")
print(f"Team lost {lost} games.")
print(f"Drawn games: {draw}")