#Read User Input
t_shirt_price = float(input())
target = float(input())

#Logic

shorts = t_shirt_price * 0.75
socks = shorts * 0.2
boots = (t_shirt_price + shorts) * 2
total = (t_shirt_price + shorts + socks + boots) * 0.85

#Print Output

if total >= target:
    print("Yes, he will earn the world-cup replica ball!")
    print(f"His sum is {total:.2f} lv.")
else:
    difference = target - total
    print(f"No, he will not earn the world-cup replica ball.")
    print(f"He needs {difference:.2f} lv. more.")