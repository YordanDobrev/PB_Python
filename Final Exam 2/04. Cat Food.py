#Read User Input
cats = int(input())

#Logic

group_1 = 0
group_2 = 0
group_3 = 0
total_weight = 0

for i in range(cats):
    current_weight = float(input())

    if current_weight >= 300 < 400:
        group_3 += 1
    elif current_weight >= 200 < 300:
        group_2 += 1
    elif current_weight >= 100 < 200:
        group_1 += 1

    total_weight += current_weight

#Print Output

print(f"Group 1: {group_1} cats.")
print(f"Group 2: {group_2} cats.")
print(f"Group 3: {group_3} cats.")
print(f"Price for food per day: {(total_weight/1000) * 12.45:.2f} lv.")