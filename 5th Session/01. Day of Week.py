#Read User Input
number = int(input())
day_of_the_week = "Error"

#Logic

if number == 1:
    day_of_the_week = "Monday"
elif number == 2:
    day_of_the_week = "Tuesday"
elif number == 3:
    day_of_the_week = "Wednesday"
elif number == 4:
    day_of_the_week = "Thursday"
elif number == 5:
    day_of_the_week = "Friday"
elif number == 6:
    day_of_the_week = "Saturday"
elif number == 7:
    day_of_the_week = "Sunday"

#Print Output

print(day_of_the_week)