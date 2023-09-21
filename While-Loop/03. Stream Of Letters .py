#Read User Input
command = input()

#Logic

word = ""
word_to_print = ""

secret_letter_c = False
secret_letter_o = False
secret_letter_n = False

while command != "End":

    for i in range(65, 90 + 1):
        if command == chr(i):
            if command == "c" and not secret_letter_c:
                secret_letter_c = True
                command = ""
            elif command == "o" and not secret_letter_o:
                secret_letter_o = True
                command = ""
            elif command == "n" and not secret_letter_n:
                secret_letter_n = True
                command = ""
            else:
                word += command

    for j in range(97, 122 + 1):
        if command == chr(j):
            if command == "c" and not secret_letter_c:
                secret_letter_c = True
                command = ""
            elif command == "o" and not secret_letter_o:
                secret_letter_o = True
                command = ""
            elif command == "n" and not secret_letter_n:
                secret_letter_n = True
                command = ""
            else:
                word += command

    if secret_letter_c and secret_letter_o and secret_letter_n:
        command = " "
        word += command
        if len(word) > len(word_to_print):
            word_to_print = word
        secret_letter_c = False
        secret_letter_o = False
        secret_letter_n = False

    command = input()

#Print Output


print(word_to_print)