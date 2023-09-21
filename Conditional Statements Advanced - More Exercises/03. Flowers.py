#Read User Input
hrizantems = int(input())
roses = int(input())
tulups = int(input())
season = input()
holiday = input()
bucket = 2

#Logic

hrizantems_total = 0
roses_total = 0
tulups_total = 0
flowers = hrizantems + roses + tulups

if season == "Spring":
    hrizantems_total = hrizantems * 2
    roses_total = roses * 4.10
    tulups_total = tulups * 2.50
elif season == "Summer":
    hrizantems_total = hrizantems * 2
    roses_total = roses * 4.10
    tulups_total = tulups * 2.50
else:
    hrizantems_total = hrizantems * 3.75
    roses_total = roses * 4.50
    tulups_total = tulups * 4.15

total = hrizantems_total + roses_total + tulups_total

if holiday == "Y":
    total = total + (total * 0.15)

if tulups > 7 and season == "Spring":
    total *= 0.95

if roses >= 10 and season == "Winter":
    total *= 0.90

if flowers > 20:
    total *= 0.80

bucket_price = total + bucket

#Print Output

print(f'{bucket_price:.2f}')