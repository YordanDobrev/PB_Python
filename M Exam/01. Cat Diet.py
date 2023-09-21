#Read User Input
fat_percentage = int(input()) / 100
protein_percentage = int(input()) / 100
carbohydrate_percentage = int(input()) / 100
calories = int(input())
water = int(input()) / 100

fat = 9
protein = 4
carbohydrate = 4

#Logic

fat_weight = fat_percentage * calories / fat
protein_weight = protein_percentage * calories / protein
carbohydrate_weight = carbohydrate_percentage * calories / carbohydrate
total_food = fat_weight + protein_weight + carbohydrate_weight
calories_per_gram = calories / total_food

final = abs((calories_per_gram * water) - calories_per_gram)

#Print Output

print(f"{final:.4f}")
