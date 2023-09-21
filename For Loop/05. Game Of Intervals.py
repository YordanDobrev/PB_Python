#Read User Input
intervals = int(input())

#Logic

total_points = 0
from_0_to_9 = 0
from_10_to_19 = 0
from_20_to_29 = 0
from_30_to_39 = 0
from_40_to_50 = 0
invalid_numbers = 0

for i in range(intervals):
    number = int(input())

    if number < 0 or number > 50:
        invalid_numbers += 1
        total_points /= 2
    elif number >= 40 <= 50:
        from_40_to_50 += 1
        total_points += 100
    elif number >= 30 <= 39:
        from_30_to_39 += 1
        total_points += 50
    elif number >= 20 <= 29:
        from_20_to_29 += 1
        total_points += number * 0.4
    elif number >= 10 <= 19:
        from_10_to_19 += 1
        total_points += number * 0.3
    elif number >= 0 <= 9:
        from_0_to_9 += 1
        total_points += number * 0.2

average_1 = (from_0_to_9 / intervals) * 100
average_2 = (from_10_to_19 / intervals) * 100
average_3 = (from_20_to_29 / intervals) * 100
average_4 = (from_30_to_39 / intervals) * 100
average_5 = (from_40_to_50 / intervals) * 100
average_invalid = (invalid_numbers / intervals) * 100

#Print Output

print(f"{total_points:.2f}")
print(f"From 0 to 9: {average_1:.2f}%")
print(f"From 10 to 19: {average_2:.2f}%")
print(f"From 20 to 29: {average_3:.2f}%")
print(f"From 30 to 39: {average_4:.2f}%")
print(f"From 40 to 50: {average_5:.2f}%")
print(f"Invalid numbers: {average_invalid:.2f}%")