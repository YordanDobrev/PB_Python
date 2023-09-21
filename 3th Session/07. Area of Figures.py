from math import pi

#Read User Input
shape = input()
area = 0

#Logic

if shape == "square":
    length = float(input())
    area = length * length

elif shape == "rectangle":
    side_a = float(input())
    side_b = float(input())
    area = side_b*side_a

elif shape == "circle":
    rad = float(input())
    area = (rad*rad)*pi

else:
    x = float(input())
    h = float(input())
    area = (x/2)*h

#Print Output

print(f'{area:.3f}')
