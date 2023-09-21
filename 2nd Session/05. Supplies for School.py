pen = int(input())
marker = int(input())
liquid_litres = int(input())
discount = int(input()) / 100

pen_price = pen * 5.80
markers_price = marker * 7.20
liquid_per_litre_price = liquid_litres * 1.20

checkout = pen_price + markers_price + liquid_per_litre_price
total = checkout - (checkout * discount)

print(total)

