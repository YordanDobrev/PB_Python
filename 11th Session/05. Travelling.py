#Read User Input

money = 0

#Logic

while True:
    country = input()
    if country == "End":
        break
    target = float(input())
    while True:
        current_money = float(input())
        money += current_money
        if money >= target:
            print(f"Going to {country}!")
            money = 0
            break

#Print Output