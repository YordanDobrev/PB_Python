#Read User Input
number = int(input())

counter = 1

#Logic

while True:
    if counter > number:
        break
    print(counter)
    counter = counter * 2 + 1

#Print Output