#Read User Input
age = int(input())
laundry_price = float(input())
toy_price = int(input())

toys = 0
total_summ = 0
current_summ = 0

#Logic

for i in range(1,age+1):
    if i % 2 == 0:
        current_summ += 10
        total_summ += current_summ - 1
    else:
        toys += 1

total = total_summ + (toys * toy_price)
difference = abs(total - laundry_price)

#Print Output

if total >= laundry_price:
    print(f"Yes! {difference:.2f}")
else:
    print(f"No! {difference:.2f}")