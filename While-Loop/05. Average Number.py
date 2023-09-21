#Read User Input
number = int(input())

sum = 0

#Logic

for i in range(number):
    current_number = int(input())
    sum += current_number

#Print Output

print(f"{sum / number:.2f}")