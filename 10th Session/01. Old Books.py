#Read User Input
book = input()

book_counter = 0

#Logic

while True:
    current_book = input()
    if current_book == book:
        print(f"You checked {book_counter} books and found it.")
        break
    if current_book == "No More Books":
        print(f"The book you search is not here!")
        print(f"You checked {book_counter} books.")
        break
    book_counter += 1

#Print Output