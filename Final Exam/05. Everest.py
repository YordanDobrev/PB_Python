#Read User Input
sleep = input()

sum = 5364
days = 1

#Logic

while sleep != "END":
    meters = int(input())
    if days == 5:
        break
    else:
        if sleep == "No":
            sum += meters
            if sum >= 8848:
                break
            sleep = input()
        elif sleep == "Yes":
            days += 1
            sum += meters
            if sum >= 8848:
                break
            sleep = input()

#Print Output

if sum >= 8848:
    print(f"Goal reached for {days} days!")
else:
    print(f"Failed!")
    print(sum)