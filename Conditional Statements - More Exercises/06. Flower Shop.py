from math import ceil
from math import floor

magnolia = int(input())
zumbuli = int(input())
roses = int(input())
cactus = int(input())
gift_price = float(input())

magnolia_price = 3.25
zumbuli_price = 4
roses_price = 3.50
cactus_price = 8

total = (magnolia_price * magnolia) + (zumbuli_price*zumbuli) + (roses_price*roses) + (cactus_price*cactus)
deduction = total - (total*0.05)
money_left = deduction - gift_price
money_to_borrow = gift_price - deduction

if gift_price > deduction:
    print("She will have to borrow " + str(ceil(money_to_borrow)) + " leva.")
else:
    print("She is left with " + str(floor(money_left)) + " leva.")