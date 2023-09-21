#Read User Input
tournaments = int(input())

#Logic
total_money = 0
total_wins = 0
total_losses = 0

for i in range(tournaments):
    current_day_money = 0
    current_day_lose = 0
    current_day_win = 0

    sport = input()
    while sport != "Finish":
        current_stage = input()
        if current_stage == "win":
            current_day_win += 1
            current_day_money += 20
        elif current_stage == "lose":
            current_day_lose += 1
        sport = input()

    if current_day_win > current_day_lose:
        current_day_money *= 1.10

    total_money += current_day_money
    total_wins += current_day_win
    total_losses += current_day_lose

#Print Output
if total_wins > total_losses:
    total_money *= 1.20
    print(f"You won the tournament! Total raised money: {total_money:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_money:.2f}")