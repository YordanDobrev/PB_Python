from math import ceil
#Read User Input
height = int(input())
width = int(input())
percent = int(input()) / 100

#Logic

area = (height * width * 4) - ((height * width * 4) * percent)
total = 0
paint = input()

while True:
    if paint == "Tired!":
        break

    paint = int(paint)
    total += paint

    if area <= total:
        break
    paint = input()

difference = ceil(abs(area - total))

#Print Output

if total > area:
    print(f"All walls are painted and you have {difference} l paint left!")
elif total == area:
    print("All walls are painted! Great job, Pesho!")
else:
    print(f"{difference} quadratic m left.")