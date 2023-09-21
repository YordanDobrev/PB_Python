# Read User Input
fruit = input()
day_of_the_week = input()
quantity = float(input())

total = 0

day = True

# Logic

if day_of_the_week == "Sunday" or day_of_the_week == "Saturday":
    if fruit == "banana":
        total = quantity * 2.70
    elif fruit == "apple":
        total = quantity * 1.25
    elif fruit == "orange":
        total = quantity * 0.90
    elif fruit == "grapefruit":
        total = quantity * 1.60
    elif fruit == "kiwi":
        total = quantity * 3
    elif fruit == "pineapple":
        total = quantity * 5.60
    elif fruit == "grapes":
        total = quantity * 4.2
    else:
        day = False

elif day_of_the_week == "Monday" or day_of_the_week == "Tuesday" or \
        day_of_the_week == "Wednesday" or day_of_the_week == "Thursday" or \
        day_of_the_week == "Friday":
    if fruit == "banana":
        total = quantity * 2.5
    elif fruit == "apple":
        total = quantity * 1.2
    elif fruit == "orange":
        total = quantity * 0.850
    elif fruit == "grapefruit":
        total = quantity * 1.45
    elif fruit == "kiwi":
        total = quantity * 2.70
    elif fruit == "pineapple":
        total = quantity * 5.50
    elif fruit == "grapes":
        total = quantity * 3.85
    else:
        day = False
else:
    day = False
# Print Output

if day == False:
    print("error")
else:
    print(f"{total:.2f}")
