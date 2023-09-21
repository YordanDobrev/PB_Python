from math import floor
from math import ceil

area = int(input())
grape_per_sq_meter = float(input())
wine_target = int(input())
workers = int(input())

total_grape = area*grape_per_sq_meter
wine = total_grape * 0.4 / 2.5

wine_left = wine - wine_target
wine_per_worker = wine_left / workers

wine_need = wine_target - wine

if wine >= wine_target:
    print("Good harvest this year! Total wine: " + str(floor(wine)) + " liters.")
    print(str(ceil(wine_left)) + " liters left -> " + str(ceil(wine_per_worker)) + " liters per person.")
else:
    print("It will be a tough winter! More " + str(floor(wine_need)) + " liters wine needed.")
