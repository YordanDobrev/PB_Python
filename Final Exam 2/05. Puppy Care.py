#Read User Input
dog_food = int(input()) * 1000
command = input()

#Logic

while command != "Adopted":
    command = int(command)
    dog_food -= command
    command = input()

#Print Output

if dog_food >= 0:
    print(f"Food is enough! Leftovers: {dog_food} grams.")
else:
    print(f"Food is not enough. You need {abs(dog_food)} grams more.")