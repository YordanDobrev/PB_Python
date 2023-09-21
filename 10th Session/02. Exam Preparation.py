# Read User Input
bad_score = int(input())

average_score = 0
number_of_tasks = 0
number_of_bad_scores = 0
last_task = ""
has_failed = False

# Logic
task = input()

while task != "Enough":
    score = int(input())
    if score <= 4:
        number_of_bad_scores += 1
        if number_of_bad_scores == bad_score:
            has_failed = True
            break
    number_of_tasks += 1
    average_score += score
    last_task = task
    task = input()

# Print Output

if has_failed:
    print(f"You need a break, {number_of_bad_scores} poor grades.")
else:
    average = average_score / number_of_tasks
    print(f"Average score: {average:.2f}")
    print(f"Number of problems: {number_of_tasks}")
    print(f"Last problem: {last_task}")