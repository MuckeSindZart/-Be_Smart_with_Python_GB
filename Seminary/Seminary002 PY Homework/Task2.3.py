# Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.

# *Пример:* - Для n = 6: [2.0, 2.25, 2.37037037037037, 2.44140625, 
#                               2.4883199999999994, 2.5216263717421135]

def input_numbers(inputText):
    Chek = False
    while not Chek:
        try:
            number = int(input(f"{inputText}"))
            Chek = True
        except ValueError:
            print("Это не то! Вводить надо целые числа!")
    return number

def print_our_sequence(number):

    list = [round((1 + 1/n)**n, 2) for n in range(1, n+1)]
    print(list)
    print(round(sum(list), 2))


##---------------------------------------------------------------##

n = input_numbers("Введите n: ")

print_our_sequence(n)

