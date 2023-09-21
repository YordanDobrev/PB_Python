length = int(input())
width = int(input())
height = int(input())
accessories = float(input())

aquarium = (length*width*height)/1000
water = aquarium*(1-0.17)

print(water)