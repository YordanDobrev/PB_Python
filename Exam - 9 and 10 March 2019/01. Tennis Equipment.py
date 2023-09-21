from math import floor
from math import ceil

#Read User Input
racket_price = float(input())
racket = int(input())
sneakers = int(input())
sneakers_price = racket_price / 6

#Logic

other_equipment = ((sneakers * sneakers_price) + (racket * racket_price)) * 0.2
total = other_equipment + (racket * racket_price) + (sneakers * sneakers_price)

djokovic_price = total / 8
sponsors_price = total * 7 / 8

#Print Output

print(f"Price to be paid by Djokovic {floor(djokovic_price)}")
print(f"Price to be paid by sponsors {ceil(sponsors_price)}")