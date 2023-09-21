Square_Meters = float(input())

Meter = 7.61

Total = Square_Meters * Meter
discount = round(Total*0.18,2)

Final = round(Total-discount,2)

print("The final price is: " + str(Final) + " lv.")
print("The discount is: " + str(discount) + " lv.")