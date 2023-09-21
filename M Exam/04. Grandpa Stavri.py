#Read User Input
days = int(input())

#Logic

litres = 0
degrees = 0

for i in range(days):
    rakia = float(input())
    bevarage_degrees = float(input())
    litres += rakia
    degrees += bevarage_degrees * rakia

average_degreese = degrees / litres

#Print Output

print(f"Liter: {litres:.2f}")
print(f"Degrees: {average_degreese:.2f}")

if average_degreese > 42:
    print("Dilution with distilled water!")
elif average_degreese >= 38 <= 42:
    print("Super!")
elif average_degreese < 38:
    print("Not good, you should baking!")
