# Вычислить число c заданной точностью d
#    Пример: - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

def input_numbers(inputText):
    Chek = False
    while not Chek:
        try:
            number = int(input(f"{inputText}"))
            if 1 <= number <= 15:
                Chek = True
            elif number > 15:
                print("Это не то! Вводить надо целые числа от 1 до 15!")
            elif number < 1:
                print("Это не то! Вводить надо целые числа от 1 до 15!")
        except ValueError:
            print("Это не то! Вводить надо целые числа от 1 до 15!")
    return number


def pi_row(e):
    pi, sign, m = 3, 1, 2
    while abs(pi - (pi + sign*4/(m**3+3*m**2+2*m))) > 10**(-d-1):
        pi = pi + sign*4/(m**3+3*m**2+2*m)
        sign = -1*sign
        m = m+2
    return (pi + (pi + sign*4/(m**3+3*m**2+2*m)))/2


##---------------------------------------------------------------##

d = input_numbers(
    "Введите точность (до 15ти знаков), c которой хотите вычислить Пи:")
mypi = pi_row(d)
print(f"Число Пи с заданной точностью {d} равно {round(mypi, d)}")
