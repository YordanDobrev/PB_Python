#Read User Input
username = input()
password = input()

current_text = input()

#Logic

while True:
    if password == current_text:
        print(f"Welcome {username}!")
        break
    else:
        current_text = input()

#Print Output