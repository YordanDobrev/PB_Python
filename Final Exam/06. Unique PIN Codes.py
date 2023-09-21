#Read User Input
first_number = int(input())
second_number = int(input())
third_number = int(input())

#Logic

for i in range(2, first_number + 1, 2):
    for j in range(2, second_number + 1):
        for k in range(2, third_number + 1, 2):
            if j == 2 or j == 3 or j == 5 or j == 7:
                print(f"{i} {j} {k}")

#Print Output