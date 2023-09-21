from math import ceil
from math import floor

days = int(input())
food = int(input())
dog_food = float(input())
cat_food = float(input())
turtle_food = float(input())

total_food = (dog_food + cat_food + (turtle_food/1000)) * days
food_left = abs(total_food-food)

if total_food <= food:
    print(str(floor(food_left)) + " kilos of food left.")
else:
    print(str(ceil(food_left)) + " more kilos of food are needed.")