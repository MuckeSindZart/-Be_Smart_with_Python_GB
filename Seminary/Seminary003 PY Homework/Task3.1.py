# '1. Задайте список из нескольких чисел. Напишите программу,
#    которая найдёт сумму элементов списка, стоящих на нечётной позиции.

#    *Пример:*  - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


from random import randint


def create_rnd_list(size):

    newlist = []
    for _ in range(size):
        newlist.append(randint(1, 9))
    return newlist


def sum_in_list(list):

    sum = 0
    for i in range(len(list)):
        if i % 2 != 0:
            sum += list[i]
    return sum


##---------------------------------------------------------------##

newList = create_rnd_list(5)
print(f"{newList} -> {sum_in_list(newList)} ")

newList = create_rnd_list(7)
print(f"{newList} -> {sum_in_list(newList)} ")

newList = create_rnd_list(9)
print(f"{newList} -> {sum_in_list(newList)} ")
