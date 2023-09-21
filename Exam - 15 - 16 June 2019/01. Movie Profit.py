#Read User Input
movie = input()
days = int(input())
tickets = int(input())
price_per_ticket = float(input())
cinema_tax = int(input()) / 100

#Logic

total = (days * tickets) * price_per_ticket
cinema_money = total * cinema_tax
profit = total - cinema_money

#Print Output

print(f"The profit from the movie {movie} is {profit:.2f} lv.")