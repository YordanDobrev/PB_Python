# Read User Input
charity = int(input())

total_amount = 0
average_cash = 0
average_card = 0
counter = 0
card_counter = 0
cash_counter = 0

cash = False
card = False
money = False

# Logic

while charity >= 0:
    action = input()
    counter += 1

    if action == "End":
        break

    action = int(action)

    if counter % 2 == 0 and action < 10:
        print("Error in transaction!")
        continue
    elif counter % 2 == 0:
        print("Product sold!")
        card_counter += 1
        average_card += action
        total_amount += action
        charity -= action
    elif counter % 1 == 0 and action > 100:
        print("Error in transaction!")
        continue
    elif counter % 1 == 0:
        print("Product sold!")
        cash_counter += 1
        average_cash += action
        total_amount += action
        charity -= action

    if charity <= 0:
        money = True
        break

# Print Output

if not money:
    print("Failed to collect required money for charity.")
else:
    print(f"Average CS: {average_cash/cash_counter:.2f}")
    print(f"Average CC: {average_card/card_counter:.2f}")