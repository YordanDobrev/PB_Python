#Read User Input
budget = float(input())
video_card = int(input())
processors = int(input())
ram = int(input())

#Logic

video_card_price = video_card * 250
processor_price = (video_card_price * 0.35) * processors
ram_price = (video_card_price * 0.1) * ram

total = video_card_price + processor_price + ram_price

if video_card > processors:
    total *= 0.85

money_left = abs(total-budget)

#Print Output

if budget >= total:
    print(f"You have {money_left:.2f} leva left!")
else:
    print(f"Not enough money! You need {money_left:.2f} leva more!")