#Read User Input
max_number = int(input())

#Logic

while True:
    current_number = input()
    if current_number == "Stop":
        break
    current_number = int(current_number)
    if current_number >= max_number:
        max_number = current_number
#Print Output

print(max_number)