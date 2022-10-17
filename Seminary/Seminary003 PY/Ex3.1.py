##task001-------------------------------------------------##
# Дан список. Выведите те его элементы, которые встречаются
# в списке только один раз. Элементы нужно выводить в том
# порядке, в котором они встречаются в списке.
# [1,2,3,4,4,5,5,6] -> [1,2,3,6]
""" 
from random import randint


#list = [1, 2, 3, 4, 4, 5, 5, 6]

list = [randint(1,9) for i in range(10)]
print(list)
newList = []
for i in list:
    if i not in newList:
        newList.append(i)
print(newList)
 """
##task001-------------------------------------------------##
# Задайте список. Напишите программу, которая определит,
# присутствует ли в заданном списке строк некое число.
# [''ffff'.'3rfhg','4'] -> YES
""" 
list = ['ffff', '3rfhg', '4']
chek = False
for i in list:
    try:
        int(i)
        chek = True
    except:
        pass
print(chek)
 """
##task001-------------------------------------------------##
# Напишите программу, которая определит позицию второго вхождения
# строки в списке либо сообщит, что её нет.
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"],
# ищем: "qwe",  ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"],
#  ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"],
#  ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"],
#  ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1
""" 
list = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
answer = 0
c = 0
f = 'qwet'
for i in range(len(list)):
    if list[i] == f:
        c+=1
        if c==2:
            answer=i
            break
    else:
        answer = 'No'
print(f'{list}')
print(f'ищем: {f}, ответ: {answer}')
 """
""" 
list = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
f= "qwe"
index=[i for i in range(0,len(list)) if list[i]==f]
if len(index)>1:
    print(index[1])
else:
    print('No')
  """

list = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
f = "qwe"
if list.count(f) > 1:
    i = list.index(f)
    j = list[i+1:].index(f)
    print(f'{list}')
    print(f'ищем: {f}, ответ: {j+i+1}')
else:
    print(f'{list}')
    print('No')
