#Read User Input
movie = input()
counter = 0
best_movie = ""
best_movie_score = 0
#Logic
while movie != "STOP":
    score = 0
    for i in range(len(movie)):
        current_letter = movie[i]
        if ord(current_letter) >= 97 <= 122:
            score += ord(current_letter) - (len(movie) * 2)
        elif ord(current_letter) >= 65 <= 90:
            score += ord(current_letter) - len(movie)
        elif ord(current_letter) >= 32 <= 64:
            score += ord(current_letter)
        if score > best_movie_score:
            best_movie = movie
            best_movie_score = score
    counter += 1
    if counter == 7:
        break
    movie = input()
#Print Output
if counter == 7:
    print("The limit is reached.")
print(f"The best movie for you is {best_movie} with {best_movie_score} ASCII sum.")