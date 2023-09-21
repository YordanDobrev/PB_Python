#Read User Input
budget = float(input())
actor = input()

#Logic

enough_money = True

while actor != "ACTION":

    if len(actor) <= 15:
        budget -= float(input())
    else:
        budget -= (budget * 0.2)

    if budget < 0:
        enough_money = False
        break

    actor = input()

#Print Output

if enough_money:
    print(f"We are left with {abs(budget):.2f} leva.")
else:
    print(f"We need {abs(budget):.2f} leva for our actors.")