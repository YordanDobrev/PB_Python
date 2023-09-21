#Read User Input
target = 10000

steps_per_day = 0

#Logic

while steps_per_day < target:
    action = input()
    if action == "Going home":
        current_steps = int(input())
        steps_per_day += current_steps
        break
    current_step = int(action)
    steps_per_day += current_step
difference = abs(steps_per_day - target)

#Print Output

if steps_per_day >= target:
    print("Goal reached! Good job!")
    print(f"{difference} steps over the goal!")
else:
    print(f"{difference} more steps to reach goal.")
