#Read User Input
budget = float(input())
series = int(input())

sum = 0

#Logic

for movies in range(series):
    current_movie = input()
    current_movie_price = float(input())

    if current_movie == "Thrones":
        sum += current_movie_price * 0.50
    elif current_movie == "Lucifer":
        sum += current_movie_price * 0.60
    elif current_movie == "Protector":
        sum += current_movie_price * 0.70
    elif current_movie == "TotalDrama":
        sum += current_movie_price * 0.80
    elif current_movie == "Area":
        sum += current_movie_price * 0.90
    else:
        sum += current_movie_price

#Print Output

if budget >= sum:
    difference = budget - sum
    print(f"You bought all the series and left with {difference:.2f} lv.")
else:
    difference = sum - budget
    print(f"You need {difference:.2f} lv. more to buy the series!")