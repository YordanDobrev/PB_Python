from math import floor

#Read User Input
balls = int(input())

total = 0
red_balls = 0
orange_balls = 0
yellow_balls = 0
white_balls = 0
other_balls = 0
black_balls = 0

#Logic

for i in range(balls):
    current_ball = input()

    if current_ball == "red":
        total += 5
        red_balls += 1
    elif current_ball == "orange":
        total += 10
        orange_balls += 1
    elif current_ball == "yellow":
        total += 15
        yellow_balls += 1
    elif current_ball == "white":
        total += 20
        white_balls += 1
    elif current_ball == "black":
        total = floor(total / 2)
        black_balls += 1
    else:
        other_balls += 1

#Print Output

print(f"Total points: {total}")
print(f"Red balls: {red_balls}")
print(f"Orange balls: {orange_balls}")
print(f"Yellow balls: {yellow_balls}")
print(f"White balls: {white_balls}")
print(f"Other colors picked: {other_balls}")
print(f"Divides from black balls: {black_balls}")