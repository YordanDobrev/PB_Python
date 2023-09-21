#Read User Input
guests = int(input())
price_per_guest = float(input())
budget = float(input())
cake = budget * 0.1

sum = 0

#Logic

if guests > 20:
    sum = guests * (price_per_guest * 0.75)
elif guests > 15 <= 20:
    sum = guests * (price_per_guest * 0.80)
elif guests >= 10 <= 15:
    sum = guests * (price_per_guest * 0.85)
else:
    sum = guests * price_per_guest

total = sum + cake
difference = abs(budget - total)

#Print Output

if budget >= total:
    print(f"It is party time! {difference:.2f} leva left.")
else:
    print(f"No party! {difference:.2f} leva needed.")