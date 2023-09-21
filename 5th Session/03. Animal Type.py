#Read User Input
animal = input()

output = "unknown"

#Logic

if animal == "dog":
    output = "mammal"
elif animal == "crocodile" or animal == "tortoise" or animal == "snake":
    output = "reptile"

#Print Output

print(output)