#Read User Input
strawberries_price = float(input())
banana = float(input())
orange = float(input())
berrie = float(input())
strawberries = float(input())

#Logic

berrie_price = strawberries_price / 2
orange_price = berrie_price * 0.60
banana_price = berrie_price * 0.20

total = (strawberries_price * strawberries) + (banana_price * banana) + (orange_price * orange) + (berrie_price * berrie)

#Print Output

print(f"{total:.2f}")