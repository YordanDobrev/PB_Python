#Read User Input
trip_price = float(input())
budget = float(input())

total_days = 0
spend_counter = 0

#Logic

while budget < trip_price and spend_counter < 5:
    decision = input()
    money = float(input())
    total_days += 1
    if decision == "spend":
        spend_counter += 1
        budget -= money
        if budget < 0:
            budget = 0
    elif decision == "save":
        spend_counter = 0
        budget += money

#Print Output

if spend_counter == 5:
    print("You can't save the money.")
    print(total_days)

if budget >= trip_price:
    print(f"You saved the money for {total_days} days.")