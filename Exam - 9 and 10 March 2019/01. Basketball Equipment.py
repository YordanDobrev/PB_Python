#Read User Input
tax = int(input())

#Logic

sneakers = tax * 0.6
clothes = sneakers * 0.8
ball = clothes / 4
accessories = ball / 5

total = tax + sneakers + clothes + ball + accessories

#Print Output

print(f"{total:.2f}")