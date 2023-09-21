#Read User Input
stage = input()
ticket_type = input()
tickets = int(input())
picture = input()

#Logic

total = 0

if ticket_type == "Standard":
    if stage == "Quarter final":
        total = tickets * 55.50
    elif stage == "Semi final":
        total = tickets * 75.88
    elif stage == "Final":
        total = tickets * 110.10
elif ticket_type == "Premium":
    if stage == "Quarter final":
        total = tickets * 105.20
    elif stage == "Semi final":
        total = tickets * 125.22
    elif stage == "Final":
        total = tickets * 160.66
elif ticket_type == "VIP":
    if stage == "Quarter final":
        total = tickets * 118.90
    elif stage == "Semi final":
        total = tickets * 300.40
    elif stage == "Final":
        total = tickets * 400

if total > 4000:
    total *= 0.75
elif total > 2500 <= 4000:
    total *= 0.90
    if picture == "Y":
        total += tickets * 40
else:
    if picture == "Y":
        total += tickets * 40

#Print Output

print(f"{total:.2f}")
