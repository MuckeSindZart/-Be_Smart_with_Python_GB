# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
# 2*x² + 4*x + 5 3*x² +10*x + 6 Вывод: 5*x² + 14*x + 11

import sympy


with open('poly1.txt', 'r') as data:
    poly1 = data.readline().split(' = ')
print(poly1)
data.close()

with open('poly2.txt', 'r') as data:
    poly2 = data.readline().split(' = ')
print(poly2)
data.close()

#poly1 = ['16*x**2 + 5*x**1 + 11', '0']             ## для примера
#poly2 = ['15*x**3 + 20*x**2 + 15*x**1 + 5', '0']

poly_summ = sympy.simplify(poly1[0]+'+'+poly2[0])

with open('poly_summ.txt', 'w') as data:
    data.write(f'{poly_summ}' + f" = {int(poly1[1]) + int(poly2[1])}")
data.close()

with open('poly_summ.txt', 'r') as data:
    prnt = data.readline()
    print(prnt)
data.close()
