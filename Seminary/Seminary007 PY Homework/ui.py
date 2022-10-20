import logger
import model

def menu():
    return int(input(f'Запись\t\t\t-1\nПоиск\t\t\t-2\nОткрыть справочник\t-3\nВыбор:'))

while True:
    select = menu()
    if select == 1:
        logger.write_in_book(f'{model.new_contact()}')
    elif select == 2:
        contact = model.request()
        book = logger.get_book()
        print()
        print(model.find_contact(book, contact))
    elif select == 3:
        print()
        print(''.join(logger.get_book()))
        