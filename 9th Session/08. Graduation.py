#Read User Input
student = input()

average = 0
fail_counter = 0
student_class = 1


#Logic
while True:
    current_grade = float(input())
    if current_grade < 4:
        fail_counter += 1
        if fail_counter > 1:
            print(f"{student} has been excluded at {student_class} grade")
            break
        continue
    student_class +=1
    average += current_grade

    if student_class > 12:
        print(f"{student} graduated. Average grade: {average / 12:.2f}")
        break

#Print Output

