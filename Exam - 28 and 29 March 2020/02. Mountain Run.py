from math import floor
#Read User Input

record = float(input())
distance = float(input())
time_per_m = float(input())

#Logic

george = distance * time_per_m
incline = floor(distance / 50) * 30
total_time = george + incline

#Print Output

if total_time >= record:
    difference = total_time - record
    print(f"No! He was {difference:.2f} seconds slower.")
else:
    print(f"Yes! The new record is {total_time:.2f} seconds.")