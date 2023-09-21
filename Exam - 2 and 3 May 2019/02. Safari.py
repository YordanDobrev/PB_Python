#Read User Input
budget = float(input())
petrol = float(input()) * 2.10
day = input()

#Logic

total = petrol + 100

if day == "Saturday":
    total *= 0.9
elif day == "Sunday":
    total *= 0.8

#Print Output

if total <= budget:
    difference = budget - total
    print(f"Safari time! Money left: {difference:.2f} lv.")
else:
    difference = total - budget
    print(f"Not enough money! Money needed: {difference:.2f} lv.")