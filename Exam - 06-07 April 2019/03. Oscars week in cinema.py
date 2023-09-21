#Read User Input
movie = input()
type = input()
tickets = int(input())

#Logic

sum = 0

if type == "normal":
    if movie == "A Star Is Born":
        sum = tickets * 7.50
    elif movie == "Bohemian Rhapsody":
        sum = tickets * 7.35
    elif movie == "Green Book":
        sum = tickets * 8.15
    elif movie == "The Favourite":
        sum = tickets * 8.75
elif type == "luxury":
    if movie == "A Star Is Born":
        sum = tickets * 10.50
    elif movie == "Bohemian Rhapsody":
        sum = tickets * 9.45
    elif movie == "Green Book":
        sum = tickets * 10.25
    elif movie == "The Favourite":
        sum = tickets * 11.55
elif type == "ultra luxury":
    if movie == "A Star Is Born":
        sum = tickets * 13.50
    elif movie == "Bohemian Rhapsody":
        sum = tickets * 12.75
    elif movie == "Green Book":
        sum = tickets * 13.25
    elif movie == "The Favourite":
        sum = tickets * 13.95

#Print Output

print(f"{movie} -> {sum:.2f} lv.")