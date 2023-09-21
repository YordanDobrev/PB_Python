#Read User Input
movie = input()
package = input()
tickets = int(input())

bill = 0

#Logic

if movie == "John Wick":
    if package == "Drink":
        bill = tickets * 12
    elif package == "Popcorn":
        bill = tickets * 15
    elif package == "Menu":
        bill = tickets * 19
elif movie == "Star Wars":
    if package == "Drink":
        bill = tickets * 18
    elif package == "Popcorn":
        bill = tickets * 25
    elif package == "Menu":
        bill = tickets * 30
elif movie == "Jumanji":
    if package == "Drink":
        bill = tickets * 9
    elif package == "Popcorn":
        bill = tickets * 11
    elif package == "Menu":
        bill = tickets * 14

if movie == "Star Wars" and tickets >= 4:
    bill *= 0.7
elif movie == "Jumanji" and tickets == 2:
    bill *= 0.85

#Print Output

print(f"Your bill is {bill:.2f} leva.")