# 4. Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).


def input_numbers(inputText):
    Chek = False

    while not Chek:
        try:
            number = int(input(f"{inputText}"))
            Chek = True
        except ValueError:
            print("Это не то! Вводить надо целые числа!")
    return number


def check_limit_quarter(qrtr):

    if qrtr == 1:
        print('X > 0 - (+∞);' '\n' 'Y > 0 - (+∞);')
    elif qrtr == 2:
        print('X < 0 - (-∞);' '\n' 'Y > 0 - (+∞);')
    elif qrtr == 3:
        print('X < 0 - (-∞);' '\n' 'Y < 0 - (-∞);')
    else:
        print(('X > 0 - (+∞);' '\n' 'Y < 0 - (-∞);'))


##---------------------------------------------------------------##

qrtr = input_numbers('Номер четверти: ')


while qrtr < 1 or qrtr > 4:
    qrtr = input_numbers('Есть только 4 четверти: ')

check_limit_quarter(qrtr)