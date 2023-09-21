#Read User Input
time = int(input())
walks = int(input())
calories = int(input()) / 2

#Logic

minutes = walks * time
burnt_calories = minutes * 5

#Print Output

if burnt_calories >= calories:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {burnt_calories}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {burnt_calories}.")
