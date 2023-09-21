from math import floor
holiday = int(input())

working_days = 365 - holiday
seconds = (24 * 3600)
minutes = seconds // 60
hour = seconds // 3600

play_working_days = working_days * 63
play_holidays = holiday * 127
year = play_holidays+play_working_days

total_time = abs((30000-year)/60)
total_minutes = abs(floor(total_time)*60)
final = abs((30000-year))-total_minutes

if year <= 30000:
    print("Tom sleeps well")
    print(str(floor(total_time)) + " hours and " + str(final) + " minutes less for play")
else:
    print("Tom will run away")
    print(str(floor(total_time)) + " hours and " + str(final) + " minutes more for play")