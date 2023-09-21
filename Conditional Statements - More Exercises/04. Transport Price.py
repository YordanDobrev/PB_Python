kilometers = int(input())
time_of_the_day = input()

taxi_day = 0.70 + (0.79 * kilometers)
taxi_night = 0.70 + (0.90 * kilometers)
bus = 0.09 * kilometers
train = 0.06 * kilometers

if kilometers <= 19:
       if time_of_the_day == "day":
        print(f'{taxi_day:.2f}')
       elif time_of_the_day == "night":
        print(f'{taxi_night:.2f}')
elif kilometers >= 100:
        print(f'{train:.2f}')
else:
    print(f'{bus:.2f}')
