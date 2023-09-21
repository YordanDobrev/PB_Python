#Read User Input
movie = float(input())
statists = int(input())
statists_costume_price = float(input())

#Logic

decor = movie - (movie * 0.90)
clothes = statists * statists_costume_price

if statists > 150:
    clothes *= 0.90

total = clothes + decor
money_left = abs(movie-total)

#Print Output

if movie >= total:
    print("Action!")
    print(f'Wingard starts filming with {money_left:.2f} leva left.')
else:
    print("Not enough money!")
    print(f'Wingard needs {money_left:.2f} leva more.')
