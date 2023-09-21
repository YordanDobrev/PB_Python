#Read User Input
numbers = int(input())

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

#Logic

for i in range(numbers):
    current_number = int(input())
    if current_number < 200:
        p1 += 1
    elif current_number < 400:
        p2 += 1
    elif current_number < 600:
        p3 += 1
    elif current_number < 800:
        p4 += 1
    elif current_number >= 800:
        p5 += 1

p1_percentage = p1 / numbers * 100
p2_percentage = p2 / numbers * 100
p3_percentage = p3 / numbers * 100
p4_percentage = p4 / numbers * 100
p5_percentage = p5 / numbers * 100

#Print Output

print(f"{p1_percentage:.2f}%")
print(f"{p2_percentage:.2f}%")
print(f"{p3_percentage:.2f}%")
print(f"{p4_percentage:.2f}%")
print(f"{p5_percentage:.2f}%")