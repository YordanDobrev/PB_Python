from math import ceil

#Read User Input
days = int(input())
food = float(input())

#Logic

biscuit = 0
total_cat = 0
total_dog = 0
biscuit_grams = 0
total_food = 0

for i in range(days):
    dog_food = int(input())
    cat_food = int(input())

    biscuit += 1
    total_cat += cat_food
    total_dog += dog_food
    total_food += dog_food + cat_food

    if biscuit == 3:
        biscuit_grams += (dog_food + cat_food) * 0.1
        biscuit = 0

food_eaten = ((total_food / food) * 100)
dog_food_eaten = (total_dog / total_food) * 100
cat_food_eaten = (total_cat / total_food) * 100

#Print Output

print(f"Total eaten biscuits: {round(biscuit_grams)}gr.")
print(f"{food_eaten:.2f}% of the food has been eaten.")
print(f"{dog_food_eaten:.2f}% eaten from the dog.")
print(f"{cat_food_eaten:.2f}% eaten from the cat.")