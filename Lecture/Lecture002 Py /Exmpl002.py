##ex001-------------------------------------------------##

""" 'a','r','w' """

""" colors = ['red', 'green', 'blue']
data = open('file.txt', 'a')
data.writelines(colors)
data.write('\nline2\n')
data.write('line12\n')
data.close()

path = 'file.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()

with open('file.txt','a') as data:
    data.write('line221\n')
    data.write('line121\n') """

##ex002-------------------------------------------------##


""" def new_string(symbol, count=3):
    return symbol*count


print(new_string('!', 5))  # !!!!!
print(new_string('!'))  # !!!
print(new_string(4))  # 12


def con(*params):
    res: str = ''
    for item in params:
        res += item
    return res


print(con('a', 's', 's'))
print(con('a', 's', '4'))
# print(con('a', 's', 4)) TypeError
# print(con(1, 2, 4))  """

##ex003-------------------------------------------------##

""" def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n-1)+fib(n-2)

list = []
for e in range(1,20):
    list.append(fib(e))
print(list) """

##ex004-------------------------------------------------##

""" a = (3, 4)
print(a)
print(a[-1])
print(type(a)) """

##ex005-------------------------------------------------##

""" dict = {}
dict =\
    {
        'up': '1',
        'left': '2',
        'down': '3',
        'right': '4'
    }

print(dict)
print(dict['left'])

for k in dict.keys():
    print(k)

for k in dict.values():
    print(k) """

##ex006-------------------------------------------------##

""" colors = {'red', 'green', 'blue'}
print(type(colors))
print(colors)
colors.add('red')
print(colors)
colors.add('gray')
print(colors)
colors.discard('red')
print(colors)
colors.clear()
print(colors)
colors.add('ups')
print(colors) """

##ex007-------------------------------------------------##

""" a = {1, 2, 3, 4, 5, 6}
b = {2, 5, 7, 9, 0, 99}
c = a.copy()
print(c)
u = a.union(b)
print(u)
i = a.intersection(b)
print(i)
df = a.difference(b)
print(df)
df1 = b.difference(a)
print(df1) """

##ex008-------------------------------------------------##

list1 = [1, 2, 3, 4]
list2 = list1

list1[0] = 's'
list2[-1] = 's'

for e in list1:
    print(e)

print()

for e in list2:
    print(e)

print(list1.pop(2))
print(list1)

print(list1.insert(2, 'a'))
print(list1)

print(list1.append('s'))
print(list1)

