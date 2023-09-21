#Read User Input
movie_time = int(input())
scenes = int(input())
scenes_time = int(input())
preparation = movie_time * 0.15

#Logic

total = scenes * scenes_time + preparation
difference = abs(total - movie_time)

#Print Output

if movie_time > total:
    print(f"You managed to finish the movie on time! You have {round(difference)} minutes left!")
else:
    print(f"Time is up! To complete the movie you need {round(difference)} minutes.")