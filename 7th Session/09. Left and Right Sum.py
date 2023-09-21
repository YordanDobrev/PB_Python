#Read User Input
n = int(input())

left_sum = 0
right_sum = 0

#Logic

for i in range(n):
    num = int(input())
    left_sum += num

for i in range(n):
    num = int(input())
    right_sum += num

diff = abs(right_sum-left_sum)

#Print Output

if right_sum == left_sum:
    print(f'Yes, sum = {right_sum}')
else:
    print(f"No, diff = {diff}")