#Read User Input
budget = float(input())
product = input()

#Logic

items = 0
total = 0
lucky_item = 0
no_budget = False

while product != "Stop":
    product_price = float(input())
    lucky_item += 1
    items += 1

    if lucky_item == 3:
        product_price /= 2
        lucky_item = 0

    if product_price > budget:
        print(f"You don't have enough money!")
        print(f"You need {product_price - budget:.2f} leva!")
        no_budget = True
        break
    else:
        total += product_price
        budget -= product_price

    product = input()

#Print Output

if not no_budget:
    print(f"You bought {items} products for {total:.2f} leva.")