#Read User Input
bread = int(input())

max_chef = ""
max_chef_score = 0

#Logic

for i in range(bread):
    current_chef = input()
    command = input()
    current_chef_points = 0

    while command != "Stop":
        command = int(command)
        current_chef_points += command
        command = input()

    print(f"{current_chef} has {current_chef_points} points.")

    if current_chef_points > max_chef_score:
        max_chef_score = current_chef_points
        max_chef = current_chef
        print(f"{max_chef} is the new number 1!")

#Print Output

print(f"{max_chef} won competition with {max_chef_score} points!")