#Read User Input
target = int(input())
starting_stage = target - 30
jump = int(input())
failed = 0
jumps = 0
#Logic
while failed != 3:
    jumps += 1
    if target < jump:
        break
    if jump > starting_stage:
        starting_stage += 5
        failed = 0
    else:
        failed += 1
        if failed == 3:
            break
    jump = int(input())
#Print Output
if failed == 3:
    print(f"Tihomir failed at {starting_stage}cm after {jumps} jumps.")
else:
    print(f"Tihomir succeeded, he jumped over {target}cm after {jumps} jumps.")