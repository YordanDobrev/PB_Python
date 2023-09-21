budget = float(input())
category = input()
people = int(input())

xsmall = budget - (budget*0.75)
small = budget - (budget*0.60)
medium = budget - (budget*0.50)
large = budget - (budget*0.40)
xlarge = budget - (budget*0.25)

vip_tickets = 499.99 * people
normal_tickets = 249.99 * people

if category == "Normal":
    if people >= 50:
        if xlarge >= normal_tickets:
            print("Yes! You have " + f'{xlarge-normal_tickets:.2f}' + " leva left.")
        else:
            print("Not enough money! You need " + f'{normal_tickets-xlarge:.2f}' + " leva.")
    elif people >= 25 <= 49:
        if large >= normal_tickets:
            print("Yes! You have " + f'{large-normal_tickets:.2f}' + " leva left.")
        else:
            print("Not enough money! You need " + f'{(normal_tickets-large):.2f}' + " leva.")
    elif people >= 10 <= 24:
        if medium >= normal_tickets:
            print("Yes! You have " + f'{medium-normal_tickets:.2f}' + " leva left.")
        else:
            print("Not enough money! You need " + f'{normal_tickets-medium:.2f}' + " leva.")
    elif people >= 5 <= 9:
        if small >= normal_tickets:
            print("Yes! You have " + f'{small-normal_tickets:.2f}' + " leva left.")
        else:
            print("Not enough money! You need " + f'{normal_tickets-small:.2f}'  + " leva.")
    elif people < 5:
        if xsmall >= normal_tickets:
            print("Yes! You have " + f'{xsmall-normal_tickets:.2f}' + " leva left.")
        else:
            print("Not enough money! You need " + f'{normal_tickets-xsmall:.2f}' + " leva.")

elif category == "VIP":
    if people >= 50:
        if xlarge >= vip_tickets:
            print("Yes! You have " + f'{xlarge-vip_tickets:.2f}' + " leva left.")
        else:
            print("Not enough money! You need " + f'{vip_tickets-xlarge:.2f}' + " leva.")
    elif people >= 25 <= 49:
        if large >= vip_tickets:
            print("Yes! You have " + f'{large-vip_tickets:.2f}' + " leva left.")
        else:
            print("Not enough money! You need " + f'{(vip_tickets-large):.2f}' + " leva.")
    elif people >= 10 <= 24:
        if medium >= vip_tickets:
            print("Yes! You have " + f'{medium-vip_tickets:.2f}' + " leva left.")
        else:
            print("Not enough money! You need " + f'{vip_tickets-medium:.2f}' + " leva.")
    elif people >= 5 <= 9:
        if small >= vip_tickets:
            print("Yes! You have " + f'{small-vip_tickets:.2f}' + " leva left.")
        else:
            print("Not enough money! You need " + f'{vip_tickets-small:.2f}'  + " leva.")
    elif people < 5:
        if xsmall >= vip_tickets:
            print("Yes! You have " + f'{xsmall-vip_tickets:.2f}' + " leva left.")
        else:
            print("Not enough money! You need " + f'{vip_tickets-xsmall:.2f}' + " leva.")