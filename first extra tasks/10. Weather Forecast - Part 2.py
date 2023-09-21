temperature = float(input())

if temperature > 35.00:
    print("unknown")
elif temperature >= 26.00 <= 35.00:
    print("Hot")
elif temperature >= 20.10 <= 25.9:
    print("Warm")
elif temperature >= 15.00 <= 20.00:
    print("Mild")
elif temperature >= 12.00 <= 14.90:
    print("Cool")
elif temperature >= 5.00 <= 11.90:
    print("Cold")
else:
    print("unknown")
