#Read User Input
clients = int(input())
average_bill = 0
#Logic
for i in range(clients):
    current_client = input()
    items = 0
    items_price = 0
    while current_client != "Finish":
        if current_client == "basket":
            items += 1
            items_price += 1.50
        elif current_client == "wreath":
            items += 1
            items_price += 3.80
        elif current_client == "chocolate bunny":
            items += 1
            items_price += 7
        current_client = input()
    if items % 2 == 0:
        items_price *= 0.8
    average_bill += items_price
    print(f"You purchased {items} items for {items_price:.2f} leva.")
average_bill /= clients
#Print Output
print(f"Average bill per client is: {average_bill:.2f} leva.")