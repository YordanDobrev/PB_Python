#Read User Input
number = int(input())

current_number = 1
is_current_number_bigger = False

#Logic

for row in range(1, number + 1):
    for col in range(1, row + 1):
        if current_number > number:
            is_current_number_bigger = True
            break
        print(str(current_number) + " ", end="")
        current_number += 1
    if is_current_number_bigger:
        break
    print()

#Print Output