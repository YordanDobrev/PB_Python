#Read User Input
eggs = int(input())

red = 0
orange = 0
blue = 0
green = 0

max_egg = ""
max_count = 0

#Logic

for i in range(eggs):
    current_egg = input()

    if current_egg == "red":
        red += 1
        if red > max_count:
            max_egg = "red"
            max_count = red
    elif current_egg == "orange":
        orange += 1
        if orange > max_count:
            max_egg = "orange"
            max_count = orange
    elif current_egg == "blue":
        blue += 1
        if blue > max_count:
            max_egg = "blue"
            max_count = blue
    elif current_egg == "green":
        green += 1
        if green > max_count:
            max_egg = "green"
            max_count = green

#Print Output

print(f"Red eggs: {red}")
print(f"Orange eggs: {orange}")
print(f"Blue eggs: {blue}")
print(f"Green eggs: {green}")
print(f"Max eggs: {max_count} -> {max_egg}")

