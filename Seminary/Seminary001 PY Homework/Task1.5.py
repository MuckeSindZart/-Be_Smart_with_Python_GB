# Напишите программу, которая принимает на вход координаты двух точек и 
# находит расстояние между ними в 2D пространстве.

#  Пример: - A (3,6); B (2,1) -> 5,09 ; - A (7,-5); B (1,-1) -> 7,21 ; 

def input_numbers(x):
    xy = ["X", "Y"]
    a = []
    for i in range(x):
        is_OK = False
        while not is_OK:
            try:
                number = int(input(f"Введите координату по {xy[i]}: "))
                a.append(number)
                is_OK = True
            except ValueError:
                print("Это не то! Вводить надо числа!")
    return a


def calcLengthSegment(a, b):
    lengthSegment = ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** (0.5)
    return lengthSegment


##---------------------------------------------------------------##

print("Введите координаты точки А")
pointA = input_numbers(2)

print("Введите координаты точки В")
pointB = input_numbers(2)

print(f"Длина отрезка: {format(calcLengthSegment(pointA, pointB), '.2f')}")