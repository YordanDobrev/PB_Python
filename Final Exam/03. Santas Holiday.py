#Read User Input
days = int(input()) - 1
accommodation = input()
score = input()

#Logic

total = 0

if accommodation == "apartment":
    if days > 15:
        total = (days * 25) * 0.50
    elif days >= 10 <= 15:
        total = (days * 25) * 0.65
    elif days < 10:
        total = (days * 25) * 0.70
elif accommodation == "president apartment":
    if days > 15:
        total = (days * 35) * 0.80
    elif days >= 10 <= 15:
        total = (days * 35) * 0.85
    elif days < 10:
        total = (days * 35) * 0.90
else:
    total = days * 18

if score == "positive":
    total += total * 0.25
else:
    total -= total * 0.1

#Print Output

print(f"{total:.2f}")