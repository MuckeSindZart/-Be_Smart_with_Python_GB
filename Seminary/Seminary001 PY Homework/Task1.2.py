# Напишите программу для проверки истинности
# утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


def input_numbers(x):

    xyz = ["X", "Y", "Z"]
    a = []
    for i in range(x):
        a.append(input(f"Введите значение {xyz[i]}: "))
    return a


def check_boolean_expression(x):

    left = not (x[0] or x[1] or x[2])
    right = not x[0] and not x[1] and not x[2]
    result = left == right
    return result


##---------------------------------------------------------------##

for x in range(2):
    for y in range(2):
        for z in range(2):
            if not (x or y or z) == (not x and not y and not z):
                print(x, y, z, '-> "¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z" -> ',
                      not (x or y or z) == (not x and not y and not z))

expression = input_numbers(3)

if check_boolean_expression(expression) == True:
    print(f"Истина")
else:
    print(f"Ложно")
