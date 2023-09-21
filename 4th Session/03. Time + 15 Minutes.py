#Read User Input
hours = int(input())
minutes = int(input())

#Logic

extra_minutes = 15
time_m = (minutes + extra_minutes) % 60
time_h = hours + (minutes + extra_minutes) // 60

if time_h <= 23:
    print(f'{time_h}:{time_m:02d}')
else:
    print(f'0:{time_m:02d}')
#Print Output