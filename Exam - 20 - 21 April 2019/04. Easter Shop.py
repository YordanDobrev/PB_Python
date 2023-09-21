#Read User Input
total_eggs = int(input())
command = input()

total = 0

#Logic

while command != "Close":
    current_amount = int(input())

    if command == "Buy":
        if current_amount > total_eggs:
            print(f"Not enough eggs in store!")
            print(f"You can buy only {total_eggs}.")
            break
        total_eggs -= current_amount
        total += current_amount
    elif command == "Fill":
        total_eggs += current_amount

    command = input()

#Print Output

if command == "Close":
    print(f"Store is closed!")
    print(f"{total} eggs sold.")