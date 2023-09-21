#Read User Input
n_1 = int(input())
n_2 = int(input())
n_3 = int(input())

#Logic

for i in range(2, n_1 + 1, 2):
    for j in range(2, n_2 + 1):
        for k in range(2, n_3 + 1, 2):
            if j == 2 or j == 3 or j == 5 or j == 7:
                print(f"{i} {j} {k}", end="")
                print()

#Print Output