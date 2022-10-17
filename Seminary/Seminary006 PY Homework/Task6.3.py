# Задача Напишите программу, которая принимает на вход два числа 
# и проверяет, является ли одно число квадратом другого.

num1 = int(input('Введите a:'))
num2 = int(input('Введите b:'))

chek_square = lambda a , b: a**2==b or b**2 == a

print(chek_square(num1,num2))