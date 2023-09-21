#Read User Input
first_letter = input()
second_letter = input()
end_letter = input()

#Logic

count = 0

for i in range(ord(first_letter), ord(second_letter) + 1):
    for j in range(ord(first_letter), ord(second_letter) + 1):
        for k in range(ord(first_letter), ord(second_letter) + 1):
            if ord(end_letter) == i or ord(end_letter) == j or ord(end_letter) == k:
                continue
            else:
                count += 1
                print(f"{chr(i)}{chr(j)}{chr(k)}", end=" ")

#Print Output

print(count)