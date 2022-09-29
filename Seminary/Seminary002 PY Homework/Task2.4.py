# Задайте список из 2N+1 элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции вводятся с клавиатуры.


def input_numbers(inputText):
    Chek = False

    while not Chek:
        try:
            number = int(input(f"{inputText}"))
            Chek = True
        except ValueError:
            print("Это не то! Вводить надо целые числа!")
    return number


def get_digit_sequence(number):
    list = []
    step = 1
    start = -number
    stop = number+1
    if n < 0:
        step = -1
        stop -= 2
    for i in range(start, stop, step):
        list.append(i)
    return list


def calc_result(sequence, pos):
    result = 1
    for i in range(len(pos)):
        result *= sequence[int(pos[i])]
        
    return result


##---------------------------------------------------------------##

n = input_numbers('Введите N, значение для формирования списка: ')
pos = input(f'Введите, через запятую, индексы которые необходимо перемножить,от 0 до {(n*2)}: ').split(',')

sequence = get_digit_sequence(n)
print(sequence)

print(f'Произведение чисел с индексами {pos} равно {calc_result(sequence, pos)}')
