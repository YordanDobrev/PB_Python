from math import floor

length = float(input())
width = float(input())

width_size = floor(((width*100) - 100) / 70)
length_size = floor((length*100) / 120)

print(length_size*width_size-3)