import sys

# Read User Input
movies = int(input())

worse_movie = input()
worse_movie_rating = float(input())
top_movie = worse_movie
top_movie_rating = worse_movie_rating

sum_rating = worse_movie_rating

# Logic

for i in range(1,movies-1):
    current_movie = input()
    current_movie_rating = float(input())
    sum_rating += current_movie_rating

    if current_movie_rating > top_movie_rating:
        top_movie = current_movie
        top_movie_rating = current_movie_rating

    if current_movie_rating < worse_movie_rating:
        worse_movie_rating = current_movie_rating
        worse_movie = current_movie

# Print Output

print(f"{top_movie} is with highest rating: {top_movie_rating}")
print(f"{worse_movie} is with lowest rating: {worse_movie_rating}")
print(f"Average rating: {sum_rating / movies:.1f}")
