#Read User Input
budget = float(input())
profit_per_day = float(input())
deductions = float(input())
gift_price = float(input())

#Logic

total = (budget * 5) + (profit_per_day * 5) - deductions

#Print Output

if total >= gift_price:
    print(f"Profit: {total:.2f} BGN, the gift has been purchased.")
else:
    difference = abs(gift_price - total)
    print(f"Insufficient money: {difference:.2f} BGN.")