#Read User Input
fruit = input()
set_size = input()
quantity = int(input())

#Logic

total = 0

if set_size == "small":
    if fruit == "Watermelon":
        total = (2 * 56) * quantity
    elif fruit == "Mango":
        total = (2 * 36.66) * quantity
    elif fruit == "Pineapple":
        total = (2 * 42.10) * quantity
    elif fruit == "Raspberry":
        total = (2 * 20) * quantity
elif set_size == "big":
    if fruit == "Watermelon":
        total = (5 * 28.70) * quantity
    elif fruit == "Mango":
        total = (5 * 19.60) * quantity
    elif fruit == "Pineapple":
        total = (5 * 24.80) * quantity
    elif fruit == "Raspberry":
        total = (5 * 15.20) * quantity

if total > 1000:
    total /= 2
elif total >= 400 <= 1000:
    total *= 0.85

#Print Output

print(f"{total:.2f} lv.")