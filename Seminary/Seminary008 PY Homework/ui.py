import logger
import model

chek_stop = True
while chek_stop:
    select = model.menu()
    if select == 1:
        logger.write_data(model.new_input())

    elif select == 2:
        print(model.search(logger.read_data()))

    elif select == 3:
        print(f'{logger.read_data()}\n')

    elif select == 4:
        edit_str = model.search(logger.read_data())
        while edit_str.count('\n') > 0:
            print(logger.read_data())
            edit_str = model.search(logger.read_data())
        print(edit_str)
        new_str = model.edit(edit_str)
        logger.rewrite_data('db.txt', edit_str, new_str)

    elif select == 0:
        chek_stop = False


