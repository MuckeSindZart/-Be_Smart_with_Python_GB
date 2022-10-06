# '4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

#       *Пример:* - 45 -> 101101
#                 - 3 -> 11
#                 - 2 -> 10


def input_numbers(inputText):
    Chek = False
    while not Chek:
        try:
            number = int(input(f"{inputText}"))
            Chek = True
        except ValueError:
            print("Это не то! Вводить надо целые числа!")
    return number


def binary(num):
    result = ''
    while num > 0:
        result = str(num % 2) + result
        num = num // 2
    return result


##---------------------------------------------------------------##

number = input_numbers('Введите число: ')
print(f"{number} -> {binary(number)}")
