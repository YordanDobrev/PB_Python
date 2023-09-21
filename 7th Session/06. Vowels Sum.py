#Read User Input
text = input()

sum = 0

#Logic

for i in range(len(text)):
    num = text[i]
    if text[i] == "a":
        sum += 1
    elif text[i] == "e":
        sum += 2
    elif text[i] == "i":
        sum += 3
    elif text[i] == "o":
        sum += 4
    elif text[i] == "u":
        sum += 5

#Print Output

print(sum)