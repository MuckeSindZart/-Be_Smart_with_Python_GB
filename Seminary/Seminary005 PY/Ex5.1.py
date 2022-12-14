##task001-------------------------------------------------##
# В файле находится N натуральных чисел, записанных через
# пробел. Среди чисел не хватает одного, чтобы выполнялось
# условие A[i] - 1 = A[i-1]. Найдите это число.
# Пример: Ввод: 1 2 4 5 -> 3
""" 
a = '1 2 4 5'

new_a = list(map(int, a.split()))

def check(nums):
    for i in range(1,len(nums)):
        if nums[i+1]-nums[i]>1:
            return nums[i]+1

print(f'{new_a} -> {check(new_a)}')
 """
##task002-------------------------------------------------##
# Дан список чисел. Создайте список, в который попадают
# числа, описываемые возрастающую последовательность.
# Порядок элементов менять нельзя.
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] =>
#   [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.
""" 
lst = [1, 5, 2, 3, 4, 6, 1, 7]


def get_sq(n):
    new_lst = []
    for i in range(len(n)):
        if n[i] == max(n[:i+1:]) and n[i] not in new_lst:
            new_lst.append(n[i])
    return new_lst

print(f'{lst} -> {get_sq(lst)}')
 """
##task003-------------------------------------------------##
# Напишите программу, удаляющую из текста все слова,
# содержащие "абв".
# Пример: абв абвгд гдеёжз непшщтг -> гдеёжз непшщтг

txt =  'абв абвгд гдеёжз непшщтг'
rm='абв'
txt_list = list(filter(lambda x: rm not in x, txt.split()))

print(txt)
print(txt_list)

