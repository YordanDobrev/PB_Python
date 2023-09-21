#Read User Input
budget = float(input())
destination = input()
season = input()
days = int(input())

#Logic

total = 0

if season == "Winter":
    if destination == "Dubai":
        total = (45000 * 0.7) * days
    elif destination == "Sofia":
        total = (17000 * 1.25) * days
    elif destination == "London":
        total = 24000 * days
elif season == "Summer":
    if destination == "Dubai":
        total = (40000 * 0.7) * days
    elif destination == "Sofia":
        total = (12500 * 1.25) * days
    elif destination == "London":
        total = 20250 * days

difference = abs(budget - total)

#Print Output

if budget >= total:
    print(f"The budget for the movie is enough! We have {difference:.2f} leva left!")
else:
    print(f"The director needs {difference:.2f} leva more!")