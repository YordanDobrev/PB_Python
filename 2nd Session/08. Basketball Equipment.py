tax = int(input())

snekers = tax - (tax * 0.4)
clothes = snekers - (snekers * 0.2)
ball = clothes / 4
accessories = ball / 5

total = snekers + clothes + ball + accessories + tax
print(total)