# Read User Input
num_1 = int(input())
num_2 = int(input())

# Logic

for i in range(num_1, num_2 + 1):
    for j in range(num_1, num_2 + 1):
        for k in range(num_1, num_2 + 1):
            for m in range(num_1, num_2 + 1):
                sum = j + k

                if i > m:
                    if sum % 2 == 0:
                        if i % 2 == 0 and m % 2 == 0:
                            continue
                        if i % 2 == 1 and m % 2 == 1:
                            continue
                        print(f"{i}{j}{k}{m}", end=" ")

# Print Output
