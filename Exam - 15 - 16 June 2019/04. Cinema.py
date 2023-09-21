#Read User Input
capacity = int(input())
peoples = input()

#Logic

total = 0
counter_peoples = 0
cinema_is_full = False

while peoples != "Movie time!":
    current_group = int(peoples)
    counter_peoples += current_group

    if counter_peoples > capacity:
        cinema_is_full = True
        break

    if current_group % 3 == 0:
        total += (current_group * 5) - 5
    else:
        total += current_group * 5

    peoples = input()

# Print Output

if peoples == "Movie time!":
    difference = capacity - counter_peoples
    print(f"There are {difference} seats left in the cinema.")
    print(f"Cinema income - {total} lv.")
else:
    print("The cinema is full.")
    print(f"Cinema income - {total} lv.")
