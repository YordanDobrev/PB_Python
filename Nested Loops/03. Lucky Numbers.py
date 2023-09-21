#Read User Input
lucky_number = int(input())

#Logic

for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            for l in range(1, 10):
                sum_1 = i + j
                sum_2 = k + l
                if sum_1 == sum_2:
                    if lucky_number % sum_1 == 0:
                        print(f"{i}{j}{k}{l}", end=" ")
#Print Output