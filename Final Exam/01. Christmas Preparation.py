#Read User Input
paper = int(input())
cloth = int(input())
glue = float(input())
discount = int(input()) / 100

#Logic

total = (paper * 5.80) + (cloth * 7.20) + (glue * 1.20)
final = total - (total * discount)

#Print Output

print(f"{final:.3f}")


