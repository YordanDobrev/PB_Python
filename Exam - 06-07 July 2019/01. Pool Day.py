from math import ceil

#Read User Input
ppls = int(input())
tax = float(input())
seat = float(input())
umbrella = float(input())

#Logic

ppls_using_umbrella = ceil(ppls / 2) * umbrella
ppls_using_seats = ceil(ppls * 0.75) * seat

sum = (ppls * tax) + ppls_using_umbrella + ppls_using_seats

#Print Output

print(f"{sum:.2f} lv.")