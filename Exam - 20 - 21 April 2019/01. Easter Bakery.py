#Read User Input
wheat_price = float(input())
wheat_weight = float(input())
sugar_weight = float(input())
eggs = int(input())
yeast = int(input())

#Logic

sugar_price = wheat_price * 0.75
eggs_price = wheat_price * 1.10
yeast_price = sugar_price * 0.2

total = (wheat_weight * wheat_price) + (sugar_price*sugar_weight) + (eggs_price * eggs) + (yeast * yeast_price)

#Print Output

print(f"{total:.2f}")