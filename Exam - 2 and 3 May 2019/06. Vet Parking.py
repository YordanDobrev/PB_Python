#Read User Input
days = int(input())
hours = int(input())

#Logic
total = 0
for i in range(1, days + 1):
    current_day = 0
    for j in range(1, hours + 1):
        if i % 2 == 0 and j % 2 == 1:
            total += 2.50
            current_day += 2.50
        elif i % 2 == 1 and j % 2 == 0:
            total += 1.25
            current_day += 1.25
        else:
            total += 1
            current_day += 1
    print(f"Day: {i} - {current_day:.2f} leva")

#Print Output
print(f"Total: {total:.2f} leva")