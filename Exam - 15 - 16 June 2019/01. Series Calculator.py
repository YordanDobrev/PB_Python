#Read User Input
series = input()
seasons = int(input())
movie = int(input())
time = float(input())
commercials = time * 0.2

#Logic
episode = time + commercials
extra_time = seasons * 10

total = (seasons * movie) * episode + extra_time

#Print Output

print(f"Total time needed to watch the {series} series is {int(total)} minutes.")