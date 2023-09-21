#Read User Input
starting_number = int(input())
final_number = int(input())
magic_number = int(input())

counter = 0

combination_found = False

#Logic

for i in range(starting_number, final_number + 1):
    for j in range(starting_number, final_number + 1):
        counter += 1
        sum = i + j
        if sum == magic_number:
            print(f"Combination N:{counter} ({i} + {j} = {magic_number})")
            combination_found = True
            break
    if combination_found:
        break

#Print Output

if not combination_found:
    print(f"{counter} combinations - neither equals {magic_number}")