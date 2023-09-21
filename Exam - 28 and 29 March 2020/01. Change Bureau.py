#Read User Input
btc = int(input())
yuan = float(input())
tax = float(input()) / 100

#Logic

btc_price = 1168
usd = 1.76
yuan_price = 0.15 * usd
eur = 1.95

commission = (((btc * btc_price) + (yuan * yuan_price)) / eur) * tax

total = (((btc * btc_price) + (yuan * yuan_price)) / eur) - commission

#Print Output

print(f"{total:.2f}")
