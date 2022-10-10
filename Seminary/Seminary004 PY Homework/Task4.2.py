# Задайте натуральное число N.
# Напишите программу, которая составит
# список простых множителей числа N.

def input_numbers(inputText):
    Chek = False
    while not Chek:
        try:
            number = int(input(f"{inputText}"))
            Chek = True
        except ValueError:
            print("Это не то! Вводить надо натуральные числа!")
    return number


def fill_simp_list(n):
    i = 2
    simple_list = []
    while i <= n:
        if n % i == 0:
            simple_list.append(i)
            n //= i
            i = 2
        else:
            i += 1
    return simple_list

##---------------------------------------------------------------##

n = input_numbers('Введите число N: ')
simple_list = fill_simp_list(n)
print(simple_list)
