#Read User Input
kozinak = int(input())
eggs = int(input())
cookies = int(input())

#Logic

total = (kozinak * 3.20) + (eggs * 4.35) + (cookies * 5.40) + ((eggs * 12) * 0.15)

#Print Output

print(f"{total:.2f}")