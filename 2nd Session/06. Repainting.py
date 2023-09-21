plastic = int(input())+2
paint = int(input())
thinner = int(input())
labour = int(input())

plastic_per_sq_meter = 1.50 * plastic
paint_thinner = 5 * thinner
paint_price = 14.50 * (paint+(paint * 0.10))

checkout = plastic_per_sq_meter + paint_thinner + paint_price + 0.40
total = ((checkout * 0.3)*labour) + checkout


print(total)