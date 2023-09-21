#Read User Input
width = int(input())
length = int(input())
height = int(input())

total_volume = width * length * height
total_boxes = 0
free_space = True

#Logic

while total_volume >= total_boxes:
    current_box = input()
    if current_box == "Done":
        break
    current_box = int(current_box)
    total_boxes += current_box
    if total_boxes >= total_volume:
        free_space = False
        break

difference = abs(total_volume - total_boxes)

#Print Output

if free_space:
    print(f"{difference} Cubic meters left.")
else:
    print(f"No more free space! You need {difference} Cubic meters more.")
