#Read User Input
days = int(input())
accommodation = input()
feedback = input()

total = 0

#Logic

if accommodation == "apartment":
    total = 25 * (days-1)
    if days < 10:
        total *= 0.70
    elif 10 <= days <= 15:
        total *= 0.65
    elif days > 15:
        total *= 0.50
elif accommodation == "president apartment":
    total = 35 * (days-1)
    if days < 10:
        total *= 0.90
    elif 10 <= days <= 15:
        total *= 0.85
    elif days > 15:
        total *= 0.80
elif accommodation == "room for one person":
    total = 18 * (days-1)

if feedback == "positive":
    total *= 1.25
else:
    total *= 0.9

#Print Output

print(f'{total:.2f}')