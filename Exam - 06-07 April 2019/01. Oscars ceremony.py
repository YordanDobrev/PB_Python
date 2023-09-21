#Read User Input
room_price = int(input())

#Logic

prize = room_price * 0.70
food = prize * 0.85
music = food / 2

total = room_price + prize + food + music

#Print Output

print(f"{total:.2f}")