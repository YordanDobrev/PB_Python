#Read User Input
food = int(input()) * 1000
command = input()

#Logic

total_food = 0

while command != "Adopted":
    current_grams = int(command)
    total_food += current_grams
    command = input()

difference = abs(food - total_food)

#Print Output

if food >= total_food:
    print(f"Food is enough! Leftovers: {difference} grams.")
else:
    print(f"Food is not enough. You need {difference} grams more.")