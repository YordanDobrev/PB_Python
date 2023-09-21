#Read User Input
groups = int(input())

musala = 0
monblan = 0
kilimanjaro = 0
k2 = 0
everest = 0

total_ppls = 0

#Logic

for i in range(groups):
    ppls_in_current_group = int(input())
    total_ppls += ppls_in_current_group

    if ppls_in_current_group <= 5:
        musala += ppls_in_current_group
    elif ppls_in_current_group <= 12:
        monblan += ppls_in_current_group
    elif ppls_in_current_group <= 25:
        kilimanjaro += ppls_in_current_group
    elif ppls_in_current_group <= 40:
        k2 += ppls_in_current_group
    elif ppls_in_current_group > 40:
        everest += ppls_in_current_group

percentage_musala = musala / total_ppls * 100
percentage_monblan = monblan / total_ppls * 100
percentage_kilimanjaro = kilimanjaro / total_ppls * 100
percentage_k2 = k2 / total_ppls * 100
percentage_everest = everest / total_ppls * 100

#Print Output

print(f"{percentage_musala:.2f}%")
print(f"{percentage_monblan:.2f}%")
print(f"{percentage_kilimanjaro:.2f}%")
print(f"{percentage_k2:.2f}%")
print(f"{percentage_everest:.2f}%")