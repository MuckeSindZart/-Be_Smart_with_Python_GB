# Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример: 6 -> да; 7 -> да;  1 -> нет;


def input_numbers(inputText):
    Chek = False
    while not Chek:
        try:
            number = int(input(f"{inputText}"))
            Chek = True
        except ValueError:
            print("Это не то! Вводить надо целые числа!")
    return number


def check_number(num):
    if 6 <= num <= 7:
        print("Да - Выходной.")
    elif 0 < num < 6:
        print("Нет - Будний день.")
    else:
        print("Такого дня недели не бывает.")


##---------------------------------------------------------------##

num = input_numbers("Введите число: ")
check_number(num)