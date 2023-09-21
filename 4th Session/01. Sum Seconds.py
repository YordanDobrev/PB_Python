from math import floor
#Read User Input
time_first = int(input())
time_second = int(input())
time_third = int(input())

#Logic
total_time = time_first + time_second + time_third

minutes = total_time // 60
seconds = total_time % 60

minutes = floor(minutes)

#Print Output
if seconds < 10:
    print(f'{minutes}:0{seconds}')
else:
    print(f'{minutes}:{seconds}')