#Read User Input
min_number = int(input())

#Logic

while True:
    next_number = input()

    if next_number == "Stop":
        break

    next_number = int(next_number)

    if min_number > next_number:
        min_number = next_number

#Print Output

print(min_number)