#Read User Input
cake_length = int(input())
cake_width = int(input())

total_cake = cake_width * cake_length
pieces = 0
full_cake = True

#Logic
action = input()
while True:
    if action == "STOP":
        break
    action = int(action)
    pieces += action
    if pieces >= total_cake:
        full_cake = False
        break
    action = input()

difference = (cake_width * cake_length) - pieces
#Print Output

if full_cake:
    print(f"{abs(difference)} pieces are left.")
else:
    print(f"No more cake left! You need {abs(difference)} pieces more.")