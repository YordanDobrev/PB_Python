#Read User Input
junior = int(input())
senior = int(input())
trace = input()

#Logic

players = junior + senior
junior_tax = 0
senior_tax = 0

if trace == "trail":
    junior_tax = junior * 5.50
    senior_tax = senior * 7
elif trace == "cross-country":
    if players >= 50:
        junior_tax = junior * (8 * 0.75)
        senior_tax = senior * (9.50 * 0.75)
    else:
        junior_tax = junior * 8
        senior_tax = senior * 9.50
elif trace == "downhill":
    junior_tax = junior * 12.25
    senior_tax = senior * 13.75
elif trace == "road":
    junior_tax = junior * 20
    senior_tax = senior * 21.5

total = (junior_tax+senior_tax) * 0.95

#Print Output

print(f'{total:.2f}')