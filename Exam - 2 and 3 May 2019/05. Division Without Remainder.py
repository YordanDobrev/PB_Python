#Read User Input
numbers = int(input())

p1 = 0
p2 = 0
p3 = 0

#Logic

for i in range(numbers):
    current_number = int(input())
    if current_number % 4 == 0:
        p3 += 1
    if current_number % 3 == 0:
        p2 += 1
    if current_number % 2 == 0:
        p1 += 1

p1_percentage = (p1 / numbers) * 100
p2_percentage = (p2 / numbers) * 100
p3_percentage = (p3 / numbers) * 100

#Print Output

print(f"{p1_percentage:.2f}%")
print(f"{p2_percentage:.2f}%")
print(f"{p3_percentage:.2f}%")