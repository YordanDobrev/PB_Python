from math import ceil

#Read User Input
guests = int(input())
budget = float(input())

#Logic

bread = ceil(guests / 3)
eggs = ceil(guests * 2)
total = (bread * 4) + (eggs * 0.45)
difference = abs(budget - total)
#Print Output

if budget >= total:
    print(f"Lyubo bought {bread} Easter bread and {eggs} eggs.")
    print(f"He has {difference:.2f} lv. left.")
else:
    print(f"Lyubo doesn't have enough money.")
    print(f"He needs {difference:.2f} lv. morЗдe.")