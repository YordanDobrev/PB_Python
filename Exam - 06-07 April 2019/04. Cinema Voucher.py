#Read User Input
budget = int(input())
purchase = input()

#Logic

other_purchase = 0
movie_ticket = 0
sum = 0
no_money = False

while True:
    if purchase == "End":
        break

    if len(purchase) <= 8:
        sum += ord(purchase[0])
        if sum > budget:
            no_money = True
            break
        other_purchase += 1
    else:
        sum += ord(purchase[0]) + ord(purchase[1])
        if sum > budget:
            no_money = True
            break
        movie_ticket += 1

    purchase = input()

#Print Output

print(movie_ticket)
print(other_purchase)