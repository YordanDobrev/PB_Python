#Read User Input
pvc = int(input())
pvc_type = input()
delivery = input()

sum = 60

correct_order = True

#Logic

if pvc_type == "90X130":
    if pvc < 10:
        correct_order = False
    elif pvc > 60:
        sum += pvc * (110 * 0.92)
    elif pvc > 30:
        sum += pvc * (110 * 0.95)
    else:
        sum += pvc * 110

elif pvc_type == "100X150":
    if pvc < 10:
        correct_order = False
    elif pvc > 80:
        sum += pvc * (140 * 0.90)
    elif pvc > 40:
        sum += pvc * (140 * 0.94)
    else:
        sum += pvc * 140

elif pvc_type == "130X180":
    if pvc < 10:
        correct_order = False
    elif pvc > 50:
        sum += pvc * (190 * 0.88)
    elif pvc > 20:
        sum += pvc * (190 * 0.93)
    else:
        sum += pvc * 190

elif pvc_type == "200X300":
    if pvc < 10:
        correct_order = False
    elif pvc > 50:
        sum += pvc * (250 * 0.86)
    elif pvc > 25:
        sum += pvc * (250 * 0.91)
    else:
        sum += pvc * 250

if delivery == "With delivery":
    if pvc > 99:
        sum *= 0.96
else:
    sum -= 60

#Print Output

if not correct_order:
    print("Invalid order")
else:
    print(f"{sum:.2f} BGN")