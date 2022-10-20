def new_contact():
    name = input('Имя: ')
    phone = input('Телефон: ')
    return f'{name} - {phone} \n'


def find_contact(book, request):
    for i in book:
        if request in i:
            return i


def request():
    return input('Найти: ')
