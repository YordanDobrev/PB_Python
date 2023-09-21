import random
#Read User Input
tournament = input()
#Logic
wins = 0
losses = 0
tour_count = 0
while tournament != "End of tournaments":
    matches = int(input())
    games = 0
    for i in range(matches):
        desi_team = int(input())
        opponent = int(input())
        games += 1
        if desi_team > opponent:
            difference = desi_team - opponent
            wins += 1
            print(f"Game {games} of tournament {tournament}: win with {difference} points.")
        elif desi_team < opponent:
            losses += 1
            difference = opponent - desi_team
            print(f"Game {games} of tournament {tournament}: lost with {difference} points.")
    tour_count += matches
    tournament = input()
average_win = (wins / tour_count) * 100
average_loss = (losses / tour_count) * 100
#Print Output
print(f"{average_win:.2f}% matches win")
print(f"{average_loss:.2f}% matches lost")

