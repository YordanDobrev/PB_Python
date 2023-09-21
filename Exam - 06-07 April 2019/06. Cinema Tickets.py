#Read User Input
movie = input()
#Logic
total_tickets = 0
student = 0
standard = 0
kid = 0
while movie != "Finish":
    free_seats = int(input())
    ticket = input()
    ticket_count = 0
    while ticket != "End":
        if ticket == "student":
            student += 1
        elif ticket == "standard":
            standard += 1
        elif ticket == "kid":
            kid += 1
        ticket_count += 1
        if free_seats == ticket_count:
            break
        ticket = input()
    current_movie = (ticket_count / free_seats) * 100
    total_tickets += ticket_count
    print(f"{movie} - {current_movie:.2f}% full.")
    movie = input()
#Print Output
print(f"Total tickets: {total_tickets}")
print(f"{(student / total_tickets) * 100:.2f}% student tickets.")
print(f"{(standard / total_tickets) * 100:.2f}% standard tickets.")
print(f"{(kid / total_tickets) * 100:.2f}% kids tickets.")