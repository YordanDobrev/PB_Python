from math import ceil
#Read User Input
gpu_price = int(input())
connector_price = int(input())
electricity = float(input())
profit_per_day = float(input())

#Logic

gpu_sum = gpu_price * 13
connector_sum = connector_price * 13
spend_money = gpu_sum + connector_sum + 1000
card_profit = (profit_per_day - electricity) * 13

total = spend_money / card_profit

#Print Output

print(spend_money)
print(ceil(total))