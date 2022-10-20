def write_in_book(contact):
    with open('book.txt', 'a') as file:
        file.write(contact)


def get_book():
    book = []
    with open('book.txt', 'r') as file:
        for line in file:
            book.append(line)
    return book
