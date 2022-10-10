# Задайте последовательность чисел.
# Напишите программу, которая выведет
# список неповторяющихся элементов исходной последовательности.


from random import randint


def create_rnd_new_list(size):

    newList = []
    for _ in range(size):
        newList.append(randint(1, 9))

    return newList


def unique_numbers_list(x):
    
    newList = []
    for i in x:
        if i not in newList:
            newList.append(i)
    return newList


##---------------------------------------------------------------##

list = create_rnd_new_list(20)
print(f"До: {list}")
newList = unique_numbers_list(list)
print(f"После: {newList}")
