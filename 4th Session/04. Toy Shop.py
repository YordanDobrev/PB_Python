#Read User Input
excursion = float(input())
puzzles = int(input())
dolls = int(input())
bears = int(input())
minions = int(input())
trucks = int(input())

#Logic

puzzles_price = 2.60 * puzzles
dolls_price = 3 * dolls
bears_price = 4.10 * bears
minions_price = 8.20 * minions
trucks_price = 2 * trucks

total_toys = puzzles + dolls + bears + minions + trucks
total_amount = puzzles_price + dolls_price + bears_price + minions_price + trucks_price

if total_toys >= 50:
    total_amount *= 0.75
    total_amount *= 0.90
else:
    total_amount *=0.90

#Print Output

if total_amount >= excursion:
    total_amount = total_amount - excursion
    print(f'Yes! {total_amount:.2f} lv left.')
else:
    total_amount = excursion - total_amount
    print(f'Not enough money! {total_amount:.2f} lv needed.')