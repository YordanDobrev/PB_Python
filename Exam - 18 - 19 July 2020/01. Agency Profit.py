#Read User Input
company = input()
adult = int(input())
kid = int(input())
price = float(input())
tax = float(input())

#Logic

kids_price = price * 0.3 + tax
adult_price = price + tax

total = ((kid * kids_price) + (adult_price * adult)) * 0.2

#Print Output

print(f"The profit of your agency from {company} tickets is {total:.2f} lv.")