# Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.

# *Пример:* - 6782 -> 23; - 0,56 -> 11;

def input_numbers(inputText):
    Chek = False
    while not Chek:
        try:
            number = float(input(f"{inputText}"))
            Chek = True
        except ValueError:
            print("Это не то! Вводить надо числа!")
    return number


def calc_summary_of_digits(number):
    number = str(number)
    sum = 0
    for i in number:
        if i != '.' and i != ',':
            sum += int(i)
    print(sum)


##---------------------------------------------------------------##

number = input_numbers('Enter the number: ')

calc_summary_of_digits(number)
