#Read User Input
projection_type = "Premiere" #input()
rows = 10 #int(input())
columns = 12 #int(input())

ticket_price = 0
total = 0

#Logic

if projection_type == "Premiere":
    ticket_price = 12
elif projection_type == "Normal":
    ticket_price = 7.5
elif projection_type == "Discount":
    ticket_price = 5

total = (rows * columns) * ticket_price

#Print Output

print(f'{total:.2f} leva')