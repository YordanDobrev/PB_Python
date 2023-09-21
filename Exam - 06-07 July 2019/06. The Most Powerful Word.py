# Read User Input
current_word = input()

max_word = ""
max_points = 0
current_word_points = 0

# Logic

while current_word != "End of words":
    for i in range(len(current_word)):
        current_word_text = current_word[i]
        current_letter_num = ord(current_word[i])
        current_word_points += current_letter_num

    if current_word[0] == "a" or \
            current_word[0] == "e" or \
            current_word[0] == "i" or \
            current_word[0] == "o" or \
            current_word[0] == "u" or \
            current_word[0] == "y" or \
            current_word[0] == "A" or \
            current_word[0] == "E" or \
            current_word[0] == "I" or \
            current_word[0] == "O" or \
            current_word[0] == "U" or \
            current_word[0] == "Y":
        current_word_points *= len(current_word)
    else:
        current_word_points /= len(current_word)

    if current_word_points > max_points:
        max_points = current_word_points
        max_word = current_word

    current_word_points = 0
    current_word = input()

# Print Output

print(f"The most powerful word is {max_word} - {max_points}")
