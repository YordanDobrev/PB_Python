#Read User Input
a1 = int(input())
a2 = int(input())
n = int(input())

symbol_one = a2 - 1
symbol_two = n - 1
symbol_three = int((n / 2) - 1)

#Logic

for i in range(a1, symbol_one + 1):
    for j in range(1, symbol_two + 1):
        for k in range(1, symbol_three + 1):
            sum = j + k + i
            if sum % 2 == 0:
                continue
            if i % 2 == 0:
                continue
            print(f"{chr(i)}-{j}{k}{i}")