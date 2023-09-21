import sys

#Read User Input
number = int(input())

max_number = -sys.maxsize
summ = 0

#Logic

for i in range(number):
    current_number = int(input())

    if current_number > max_number:
        max_number = current_number

    summ += current_number
#Print Output

if max_number == summ - max_number:
    print("Yes")
    print(f"Sum = {max_number}")
else:
    difference = abs(max_number - (summ-max_number))
    print("No")
    print(f"Diff = {difference}")