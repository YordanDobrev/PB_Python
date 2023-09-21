house_height = float(input())
wall_width = float(input())
roof_triangle = float(input())

#walls
front_and_back = (house_height*house_height)*2 - 2.4
sides = (house_height*wall_width)*2 - 2.25*2
green_paint = (front_and_back + sides) / 3.4

#roof
roof = ((house_height*wall_width)*2) + ((house_height / 2 ) * roof_triangle)*2
red_paint = roof / 4.3

print(f"{green_paint:.2f}")
print(f"{red_paint:.2f}")
