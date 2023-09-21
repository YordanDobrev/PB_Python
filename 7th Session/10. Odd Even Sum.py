#Read User Input
n = int(input())

even = 0
odd = 0

#Logic

for i in range(n):
    num = int(input())
    if i % 2 == 0:
        even += num
    else:
        odd += num

diff = abs(odd - even)

#Print Output

if even == odd:
    print('Yes')
    print(f'Sum = {even}')
else:
    print('No')
    print(f'Diff = {diff}')