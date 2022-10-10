# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример: - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random


def input_number(inputText):
    Chek = False
    while not Chek:
        try:
            number = int(input(f"{inputText}"))
            Chek = True
        except ValueError:
                print("Это не то! Вводить надо целые натруальные числа !")
    return number


def Polynomial(k):
    result_string = ''
    for i in range(k+1):
        if i == 0:
            result_string += \
                str(random.randint(1, 20)) + '*x**' + str(k-i)
        elif i == k:
            result_string += \
                ' + ' + str(random.randint(1, 20))
        else:
            result_string += \
                ' + ' + str(random.randint(1, 20)) + '*x**' + str(k-i)
    result_string += str(' = 0')
    return result_string


##---------------------------------------------------------------##

k = input_number(f"Введите k для 'poly1.txt' : ")
result_one = Polynomial(k)
print(result_one)

with open("poly1.txt", "w") as file:
    file.write(f'{result_one}')
file.close()

k = input_number(f"Введите k для 'poly2.txt' : ")
result_two = Polynomial(k)
print(result_two)

with open("poly2.txt", "w") as file:
    file.write(f'{result_two}')
file.close()
