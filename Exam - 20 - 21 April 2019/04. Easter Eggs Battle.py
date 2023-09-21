#Read User Input
player_one = int(input())
player_two = int(input())
player = input()

#Logic

while player != "End":

    if player == "one":
        player_two -= 1
    elif player == "two":
        player_one -= 1

    if player_one == 0 or player_two == 0:
        break

    player = input()

#Print Output

if player_one == 0:
    print(f"Player one is out of eggs. Player two has {player_two} eggs left.")
elif player_two == 0:
    print(f"Player two is out of eggs. Player one has {player_one} eggs left.")
elif player == "End":
    print(f"Player one has {player_one} eggs left.")
    print(f"Player two has {player_two} eggs left.")