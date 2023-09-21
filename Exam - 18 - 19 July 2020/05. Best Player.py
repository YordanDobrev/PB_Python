#Read User Input
player = input()

highest_player = ""
highest_score = 0
hatrick = False

#Logic

while player != "END":
    score = int(input())

    if score > highest_score:
        highest_player = player
        highest_score = score
        if highest_score >= 3:
            hatrick = True

    if highest_score >= 10:
        hatrick = True
        break

    player = input()

#Print Output

print(f"{highest_player} is the best player!")

if hatrick:
    print(f"He has scored {highest_score} goals and made a hat-trick !!!")
else:
    print(f"He has scored {highest_score} goals.")