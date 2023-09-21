#Read User Input
combination = int(input())

counter = 0

#Logic

for i in range(0, combination + 1):
    for j in range(0, combination + 1):
        for k in range(0, combination + 1):
            sum = i + j + k
            if sum == combination:
                counter += 1

#Print Output

print(counter)