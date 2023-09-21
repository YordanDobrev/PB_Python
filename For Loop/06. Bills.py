#Read User Input
months = int(input())

#Logic
electricity_bill = 0
water = 20 * months
internet = 15 * months
other = 0

for i in range(months):
    electricity = float(input())
    electricity_bill += electricity
    other += (electricity + 20 + 15) * 1.20

average = (other + electricity_bill + water + internet) / months

#Print Output

print(f"Electricity: {electricity_bill:.2f} lv")
print(f"Water: {water:.2f} lv")
print(f"Internet: {internet:.2f} lv")
print(f"Other: {other:.2f} lv")
print(f"Average: {average:.2f} lv")