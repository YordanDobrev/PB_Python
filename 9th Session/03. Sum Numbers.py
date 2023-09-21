#Read User Input
number = int(input())

sum = 0

#Logic

while True:
    if sum >= number:
        break
    current_num = int(input())
    sum += current_num

#Print Output

print(sum)