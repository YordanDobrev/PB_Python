#Read User Input
hours_exam = int(input())
minutes_exam = int(input())
hours_student = int(input())
minutes_student = int(input())

hours_exam_convert = hours_exam * 60
hours_student_convert = hours_student * 60

#Logic

time_exam = hours_exam_convert + minutes_exam
time_student = hours_student_convert + minutes_student
difference = abs(time_student - time_exam)

difference_hours = difference // 60
difference_minutes = difference % 60

#Print Output

if time_exam < time_student:
    print("Late")
    if time_exam > time_student - 60:
        print(f"{difference_minutes} minutes after the start")
    else:
        print(f"{difference_hours}:{difference_minutes:02d} hours after the start")

elif time_exam >= time_student:
    if time_exam == time_student:
        print("On Time")
    elif difference <= 30:
        print("On Time")
        print(f"{difference_minutes} minutes before the start")
    elif difference <= 59:
        print("Early")
        print(f"{difference_minutes} minutes before the start")
    elif difference >= 60:
        print("Early")
        print(f"{difference_hours}:{difference_minutes:02d} hours before the start")