#Read User Input
days = int(input())

#Logic
doctors = 7
treated = 0
untreated = 0
day = 1

for i in range(days):
    patients = int(input())
    current_status = 0
    if day == 3:
        if untreated > treated:
            doctors += 1
            day = 0
        else:
            day = 0

    if patients > doctors:
        current_status = patients - doctors
        untreated += current_status
        treated += doctors
    else:
        current_status = patients
        treated += current_status

    day += 1

#Print Output
print(f"Treated patients: {treated}.")
print(f"Untreated patients: {untreated}.")