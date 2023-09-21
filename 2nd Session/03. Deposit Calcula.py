deposit = float(input())
months = int(input())
interest = float(input()) / 100

interest_amount = deposit * interest
interest_per_month = interest_amount / 12
total = deposit + months*interest_per_month

print(total)
