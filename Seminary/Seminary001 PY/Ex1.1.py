##task001-------------------------------------------------##
# Задача: Напишите задачу, которая принимает на вход два числа и
#         проверят, является ли одно число квадратом другого.
""" 

a = int(input('Input a: '))
b = int(input('Input b: '))
#a,b = int(input('Input a: ')),int(input('Input b: '))

#c = input().split()
#a = int(c[0])
#b = int(c[1])

if a**2 == b or b**2 == a:
    print('Yes')
else:
    print('No')
 """
##task002-------------------------------------------------##
# Задача: Напишите программу, которая на фход принимает 5 чисел
#         и находит максимальное из них.
""" 
c = int(input('Input number: '))
max = c
print(f'max = {max}')
for i in range(4):
    c = int(input('Input number: '))
    if max < c:
        max = c
    print(f'max = {max}')
 """
""" 
c = list(map(int, input('Введите числа(через пробел):').split()))
print(c)
max = c[0]
for i in range(len(c)):
    if max < c[i]:
        max = c[i]

print(f'max = {max}')
 """
# some Pyhton magic
""" print(max(list(map(int, input('Введите числа(через пробел):').split())))) """

##task003-------------------------------------------------##
# Задача: Напишите программу, которая будет на вход принимать
#         число N и выводить числа от -N до N
""" 
N = int(input('Input number: '))
count = -N
mas = []
while count <= N:
    mas.append(count)
    count += 1
print(mas)
 """
""" 
N = int(input('Input number: '))
mas = []
for i in range(-N, N+1, 1):
    mas.append(i)
print(mas)
 """
##task004-------------------------------------------------##
# Задача: Напишите программу, которая будет на принимать вход
#        дробь и показывать первую цифру дробной части числа.
#            1.23->2
""" 
N = float(input('Input number: '))
print(int(N*10) % 10)
 """
""" 
N = input('Input number: ')
print(N[N.find('.')+1])
 """
##task005-------------------------------------------------##
# Задача: Напишите программу, которая будет на принимать вход
#         число и проверяет, кратно ли оно 5 и 10 или 15, но не 30

N = int(input('Input number: '))
if (N % 5 == 0 and (N % 10 == 0 or N % 15 == 0)) and N % 30 != 0:
    print('Yes')
else:
    print('No')
