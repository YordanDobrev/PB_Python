vegetables_price = float(input())
fruits_price = float(input())
vegetables_weight = int(input())
fruit_weight = int(input())

total = ((vegetables_weight*vegetables_price) + (fruit_weight*fruits_price)) / 1.94

print(f"{total:.2f}")