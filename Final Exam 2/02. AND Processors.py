from math import floor

#Read User Input

cpu = int(input())
workers = int(input())
working_days = int(input())

#Logic

hours_worked = workers * working_days * 8
cpu_created = floor(hours_worked / 3)
profit = abs(cpu - cpu_created) * 110.10

#Print Output

if cpu_created < cpu:
    print(f"Losses: -> {profit:.2f} BGN")
else:
    print(f"Profit: -> {profit:.2f} BGN")