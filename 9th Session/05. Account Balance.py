#Read User Input
money = input()

sum = 0

#Logic

while True:
    if money == "NoMoreMoney":
        break
    if float(money) < 0:
        print('Invalid operation!')
        break
    print(f'Increase: {float(money):.2f}')
    sum += float(money)
    money = input()

#Print Output

print(f'Total: {sum:.2f}')