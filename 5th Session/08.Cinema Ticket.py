#Read User Input
day = input()

ticket = 12

#Logic

if day == "Wednesday" or day == "Thursday":
    ticket = 14
elif day == "Saturday" or day == "Sunday":
    ticket = 16

#Print Output

print(ticket)