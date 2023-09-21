mekerel_price = float(input())
caca_price = float(input())
palamud_kg = float(input())
safrid_kg = float(input())
shells_kg = float(input())

palamud_price = mekerel_price + (mekerel_price * 0.6)
safrid_price = caca_price + (caca_price * 0.8)
shells_price = 7.50

total = (palamud_price*palamud_kg) + (safrid_price*safrid_kg) + (shells_price*shells_kg)

print(f"{total:.2f}")