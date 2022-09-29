from random import randint


def number_mixer(array):
    for i in range(0, len(array)-1):
        swap = array[i]
        rnd = randint(i+1, len(array)-1)
        array[i] = array[rnd]
        array[rnd] = swap
    return array


##---------------------------------------------------------------##

array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(f'Массив до:\t{array}')

array = number_mixer(array)

print(f'Массив после :\t{array}')