# '2. Напишите программу, которая найдёт произведение пар чисел списка.
#     Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#   *Пример:*
#           - [2, 3, 4, 5, 6] => [12, 15, 16];
#           - [2, 3, 5, 6] => [12, 15]


from random import randint


def create_rnd_list(size):

    newList = []
    for _ in range(size):
        newList.append(randint(1, 9))
    return newList


def calc_pairs_list(list):

    len_result = int(len(list) / 2)
    if len(list) % 2 == 1:
        len_result += 1

    result = [list[i] * list[-(i + 1)]
              for i in range(0, len_result)]
    return result


##---------------------------------------------------------------##

new_list = create_rnd_list(5)
print(f'{new_list} -> {calc_pairs_list(new_list)}')

new_list = create_rnd_list(4)
print(f'{new_list} -> {calc_pairs_list(new_list)}')

new_list = create_rnd_list(9)
print(f'{new_list} -> {calc_pairs_list(new_list)}')
