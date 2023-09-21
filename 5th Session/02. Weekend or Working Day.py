#Read User Input
day_of_the_week = input()
day = "Error"

#Logic

if day_of_the_week == "Monday" or day_of_the_week == "Tuesday" or \
        day_of_the_week == "Wednesday" or day_of_the_week == "Thursday" or\
        day_of_the_week == "Friday":
    day = "Working day"
elif day_of_the_week == "Saturday" or day_of_the_week == "Sunday":
    day = "Weekend"

#Print Output

print(day)