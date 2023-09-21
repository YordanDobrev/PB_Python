#Read User Input
money = float(input())
year = int(input())

#Logic

total = 0
ivan = 18

for i in range(1800, year + 1):
    if i % 2 == 0:
        total += 12000
    else:
        total += 12000 + (ivan * 50)

    ivan += 1

difference = abs(total - money)
#Print Output

if total > money:
    print(f"He will need {difference:.2f} dollars to survive.")
else:
    print(f"Yes! He will live a carefree life and will have {difference:.2f} dollars left.")