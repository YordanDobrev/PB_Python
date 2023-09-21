#Read User Input
stadium = int(input())
fans = int(input())

#Logic
a = 0
b = 0
v = 0
g = 0

for i in range(fans):
    sector = input()

    if sector == "A":
        a += 1
    elif sector == "B":
        b += 1
    elif sector == "V":
        v += 1
    elif sector == "G":
        g += 1

a_percent = (a / fans) * 100
b_percent = (b / fans) * 100
v_percent = (v / fans) * 100
g_percent = (g / fans) * 100
total = (fans / stadium) * 100

#Print Output
print(f"{a_percent:.2f}%")
print(f"{b_percent:.2f}%")
print(f"{v_percent:.2f}%")
print(f"{g_percent:.2f}%")
print(f"{total:.2f}%")