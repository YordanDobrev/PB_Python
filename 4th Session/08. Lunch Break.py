from math import ceil
#Read User Input
series = input()
series_time = int(input())
lunch_time = int(input())

#Logic

lunch = lunch_time * (1/8)
lunch_relax = lunch_time * (1/4)

time_left = lunch_time - lunch - lunch_relax
series_time_left = abs(time_left-series_time)

#Print Output

if time_left >= series_time:
    print(f"You have enough time to watch {series} and left with {ceil(series_time_left)} minutes free time.")
else:
    print(f"You don't have enough time to watch {series}, you need {ceil(series_time_left)} more minutes.")