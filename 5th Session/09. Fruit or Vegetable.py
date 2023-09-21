#Read User Input
user_input = input()
product = "unknown"

#Logic

if user_input == "banana" or user_input == "apple" or user_input == "kiwi" or\
        user_input == "cherry" or user_input == "lemon" or user_input == "grapes":
    product = "fruit"
elif user_input == "tomato" or user_input == "cucumber" or user_input == "pepper" or\
        user_input == "carrot":
    product = "vegetable"

#Print Output.

print(product)
