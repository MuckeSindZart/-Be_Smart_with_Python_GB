##task001-------------------------------------------------##
# Задайте строку из набора чисел. Напишите программу,
# которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел.
# Ввод: 2 3 5 -> 2 5
""" 
string = '2 3 5 45 4 -12'
new_str = list(map(int, string.split()))
maxx = new_str[0]
minn = new_str[0]
for i in new_str:
    if maxx < i:
        maxx = i
    if minn > i:
        minn = i
print(f'{new_str}')
print(f'{minn}; {maxx};')

print(f'{new_str}')
print(f'{min(new_str)}; {max(new_str)};')
 """
##task002-------------------------------------------------##
# Найдите корни квадратного уравнения Ax² + Bx + C = 0
# двумя способами:
# 1) с помощью математических формул нахождения корней
#   квадратного уравнения
# 2) с помощью дополнительных библиотек Python(sympy)
""" 
a = 2
b = -9
c = 7

d = b**2-4*a*c
if d>0:
    x1=(-b+d**0.5)/(2*a)
    x2=(-b-d**0.5)/(2*a)
    print(x1,x2)
elif d==0:
    x1=-b/(2*a)
else:
    print("Нет корней")
 """

""" from sympy.solvers import solve
 
def fun(a,b,c):
    x = 'x'
    return solve(f'{a}*x**2+{b}*x+{c}', x)
    
print('Корни уравнения:', *fun(2, -9, 7))  #  2 14
 """
##task003-------------------------------------------------##
# Задайте два числа. Напишите программу, которая найдёт
# НОК (наименьшее общее кратное) этих двух чисел.
# Ввод 3 , 10 -> 30

from math import gcd

a=int(input("a= "))
b=int(input("b= "))
print(a * b // gcd(a, b))