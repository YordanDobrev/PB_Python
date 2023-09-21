#Read User Input
luggage_price = float(input())
luggage_weight = float(input())
days = int(input())
num_luggage = int(input())

#Logic

current_price = 0

if luggage_weight > 20:
    current_price = luggage_price
elif luggage_weight >= 10 <= 20:
    current_price = luggage_price * 0.5
elif luggage_weight < 10:
    current_price = luggage_price * 0.2

if days > 30:
    current_price *= 1.10
elif days >= 7 <= 30:
    current_price *= 1.15
elif days < 7:
    current_price *= 1.40

total = current_price * num_luggage

#Print Output

print(f" The total price of bags is: {total:.2f} lv.")