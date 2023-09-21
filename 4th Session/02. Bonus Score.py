#Read User Input
number = int(input())

#Logic
points = 0


if number <= 100:
    points +=5
elif number > 1000:
    points = number * 0.1
else:
    points = number * 0.2

if number % 2 == 0:
    points+=1
elif number % 10 == 5:
    points +=2

#Print Output

print(points)
print(points+number)
