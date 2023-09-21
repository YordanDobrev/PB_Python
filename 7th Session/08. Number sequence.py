#Read User Input
n = int(input())

min_value = int(input())
max_value = min_value

#Logic

for i in range(n-1):
    number = int(input())
    if number < min_value:
        min_value = number
    if number > max_value:
        max_value = number

#Print Output

print(f'Max number: {max_value}')
print(f'Min number: {min_value}')