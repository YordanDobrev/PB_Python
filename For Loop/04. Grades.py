#Read User Input
students = int(input())

#Logic
top_students = 0
between_4_and_4_99 = 0
between_3_and_3_99 = 0
fail = 0
total = 0

for i in range(students):
    grade = float(input())

    if grade >= 5:
        top_students += 1
    elif grade >= 4 < 5:
        between_4_and_4_99 += 1
    elif grade >= 3 < 4:
        between_3_and_3_99 += 1
    else:
        fail += 1

    total += grade

average_top = (top_students / students) * 100
average_4_5 = (between_4_and_4_99 / students) * 100
average_3_4 = (between_3_and_3_99 / students) * 100
average_fail = (fail / students) * 100
average_grade = total / students

#Print Output

print(f"Top students: {average_top:.2f}%")
print(f"Between 4.00 and 4.99: {average_4_5:.2f}%")
print(f"Between 3.00 and 3.99: {average_3_4:.2f}%")
print(f"Fail: {average_fail:.2f}%")
print(f"Average: {average_grade:.2f}")