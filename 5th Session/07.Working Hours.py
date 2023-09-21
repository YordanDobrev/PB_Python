#Read User Input
time = int(input())
day = input()

works = "closed"

#Logic
if 10 <= time <= 18 and not day == "Sunday":
    works = "open"

#Print Output

print(works)