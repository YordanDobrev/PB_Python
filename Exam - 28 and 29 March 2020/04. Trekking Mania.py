#Read User Input
groups = int(input())

total_peoples = 0
musala = 0
monblan = 0
kilimanjaro = 0
k2 = 0
everest = 0

#Logic

for i in range(groups):
    current_group = int(input())
    total_peoples += current_group

    if current_group > 40:
        everest += current_group
    elif current_group >= 26 <= 40:
        k2 += current_group
    elif current_group >= 13 <= 25:
        kilimanjaro += current_group
    elif current_group >= 6 <= 12:
        monblan += current_group
    elif current_group < 6:
        musala += current_group

musala_percentage = (musala / total_peoples) * 100
monblan_percentage = (monblan / total_peoples) * 100
kilimanjaro_percentage = (kilimanjaro / total_peoples) * 100
k2_percentage = (k2 / total_peoples) * 100
everest_percentage= (everest / total_peoples) * 100

#Print Output

print(f"{musala_percentage:.2f}%")
print(f"{monblan_percentage:.2f}%")
print(f"{kilimanjaro_percentage:.2f}%")
print(f"{k2_percentage:.2f}%")
print(f"{everest_percentage:.2f}%")