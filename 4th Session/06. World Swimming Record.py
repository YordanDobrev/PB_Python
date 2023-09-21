from math import floor
#Read User Input
world_record = float(input())
distance_meters = float(input())
time_per_meter = float(input())

#Logic

distance_delay = (floor(distance_meters / 15)) * 12.5 + (distance_meters * time_per_meter)
#record = (distance_meters * time_per_meter) + distance_delay
not_succeded = abs(distance_delay - world_record)

#Print Output

if distance_delay < world_record:
    print(f'Yes, he succeeded! The new world record is {distance_delay:.2f} seconds.')
else:
    print(f'No, he failed! He was {not_succeded:.2f} seconds slower.')