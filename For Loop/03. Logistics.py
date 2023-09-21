#Read User Input
deliveries = int(input())

#Logic
total_price = 0
total_weight = 0
van = 0
truck = 0
train = 0

for i in range(deliveries):
    weight = int(input())

    if weight >= 12:
        total_price += weight * 120
        train += weight
    elif weight > 3 < 12:
        total_price += weight * 175
        truck += weight
    else:
        total_price += weight * 200
        van += weight

    total_weight += weight

average_van = (van/total_weight) * 100
average_truck = (truck/total_weight) * 100
average_train = (train/total_weight) * 100
average_price = total_price / total_weight

#Print Output

print(f"{average_price:.2f}")
print(f"{average_van:.2f}%")
print(f"{average_truck:.2f}%")
print(f"{average_train:.2f}%")