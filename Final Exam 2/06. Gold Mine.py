#Read User Input
location = int(input())

#Logic
for i in range(location):
    target = int(input())
    days_to_work = int(input())

    temp_amount = 0

    for j in range(days_to_work):
        current_amount = int(input())
        temp_amount += current_amount

    average = temp_amount / days_to_work

    if average >= target:
        print(f"Good job! Average gold per day: {average:.2f}.")
    else:
        difference = target - average
        print(f"You need {difference:.2f} gold.")

#Print Output