#Read User Input
computers = int(input())

sold = 0
average = 0
total_score = 0

#Logic

for i in range(computers):
    current_score = int(input())
    current_format_score = str(current_score)

    if current_format_score[2] == "6":
        total_score += 6
        convert = current_format_score[:2]
        sold += int(convert)
    elif current_format_score[2] == "5":
        total_score += 5
        convert = current_format_score[:2]
        sold += int(convert) * 0.85
    elif current_format_score[2] == "4":
        total_score += 4
        convert = current_format_score[:2]
        sold += int(convert) * 0.70
    elif current_format_score[2] == "3":
        total_score += 3
        convert = current_format_score[:2]
        sold += int(convert) * 0.50
    elif current_format_score[2] == "2":
        total_score += 2

average = total_score / computers

#Print Output

print(f"{sold:.2f}")
print(f"{average:.2f}")