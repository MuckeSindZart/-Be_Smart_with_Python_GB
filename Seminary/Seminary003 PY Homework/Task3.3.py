# '3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
#     между максимальным и минимальным значением дробной части элементов.

#       *Пример:*  - [1.1, 1.2, 3.1, 5.1, 10.01] => 0.19


from random import randint
from random import random


def create_rnd_list(size):

    newList = []
    for _ in range(size):
        if randint(0, 1) != 0:
            newList.append(round(randint(1, 9)+random(), 2))
        else:
            newList.append(randint(1, 9))

    return newList


def after_decimal_point(list):

    for i in range(len(list)):
        list[i] = list[i] % 1
    return list


def chek_ignore_integer(list):
    newList = []

    for i in range(len(list)):
        if list[i] % 1 != 0:
            newList.append(list[i])

    if len(newList) == 0:    # Что бы не вернуть пустой список,
        return list          # когда все числа целые,
    else:                    # (Возврат пустого списка вызывал ошибку).
        return newList


def main(list):

    tmpList = after_decimal_point(chek_ignore_integer(list))
    result = f"{max(tmpList) - min(tmpList)}"
    print(f"{list} => {result[0:4:]}")


##---------------------------------------------------------------##

list = [1.1, 1.2, 3.1, 5.1, 10.01]
main(list)
print()
main(create_rnd_list(5))
main(create_rnd_list(5))
