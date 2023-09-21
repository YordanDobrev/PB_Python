#Read User Input
town = input()
sells = float(input())

commission = 0
is_legit = True

#Logic

if town == "Sofia":
    if 0 <= sells <= 500:
        commission = sells * 0.05
    elif 500 <= sells <= 1000:
        commission = sells * 0.07
    elif 1000 <= sells <= 10000:
        commission = sells * 0.08
    elif sells > 1000:
        commission = sells * 0.12
    else:
        is_legit = False

elif town == "Varna":
    if 0 <= sells <= 500:
        commission = sells * 0.045
    elif 500 < sells <= 1000:
        commission = sells * 0.075
    elif 1000 < sells <= 10000:
        commission = sells * 0.10
    elif sells > 1000:
        commission = sells * 0.13
    else:
        is_legit = False

elif town == "Plovdiv":
    if 0 <= sells <= 500:
        commission = sells * 0.055
    elif 500 < sells <= 1000:
        commission = sells * 0.08
    elif 1000 < sells <= 10000:
        commission = sells * 0.12
    elif sells > 1000:
        commission = sells * 0.145
    else:
        is_legit = False

else:
    is_legit = False

#Print Output

if not is_legit:
    print("error")
else:
    print(f'{commission:.2f}')
