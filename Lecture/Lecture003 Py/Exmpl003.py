##ex001-------------------------------------------------##


""" def d(x):
    return x**2


g = d

print(type(d))
print(type(g))

print(d(2))
print(g(2)) """

##ex002-------------------------------------------------##


""" def calc(x):
    return x+10

print(calc(10))



def calc2(x):
    return x*10

print(calc2(10))


def math(op,x):
    print(op(x))

math(calc2,10)
math(calc,11) """

##ex003-------------------------------------------------##


""" def sum(x, y):
    return x+y


#f = lambda x,y:x+y


def mylt(x, y):
    return x*y


def calc(op, a, b):
    print(op(a, b))
    # return op(a,b)


calc(mylt, 4, 5)
calc(f, 4, 5)
calc(lambda x, y: x+y, 4, 5) """


##ex004-------------------------------------------------##


""" list = []

for i in range(1, 11):
    # if(i%2 == 0):
    list.append(i)

print(list)

list = [(i,i) for i in range(1, 21) if i % 2 == 0]
print(list)


def f(x):
    return x**3

list = [(i,f(i)) for i in range(1, 21) if i % 2 == 0]
print(list)
 """

##ex005-------------------------------------------------##


""" #path = 'txt.txt'
#f = open(path, 'r')
#data = f.read() + ' '
# f.close()


data = '1 2 3 5 8 15 23 38 '  # Вместо чтения файла

numbers = []

while data != '':
    space_pos = data.index(' ')
    numbers.append(int(data[:space_pos]))
    data = data[space_pos+1:]

out = []
for e in numbers:
    if not e % 2:
        out.append((e, e**2))
print(out) """

##ex006-------------------------------------------------##


""" def select(f, col):
    return [f(x) for x in col]


def where(f, col):
    return [x for x in col if f(x)]


data = '1 2 3 5 8 15 23 38'.split()

res = select(int, data)
print(res)
res = where(lambda x: not x % 2, res)
print(res)
res = select(lambda x: (x, x**2), res)
print(res) """

##ex007-------------------------------------------------##

""" li = [x for x in range(1, 20)]
print(li)

#li =(map(lambda x:x+10,li))
# print(li) ## <map object at 0x7ff018b21420>

li = list(map(lambda x: x+10, li)) #def asd(x): return x+10, li
print(li) """

##ex008-------------------------------------------------##

""" # data = list(map(int,input().split()))
#print(data)

data1 = map(int,'1 2 3 4'.split())

for e in data1:
    print(e)
print('#######')
for e in data1:
    print(e) """
##ex009-------------------------------------------------##

""" def where(f, col):
    return [x for x in col if f(x)]

data = '1 2 3 5 8 15 23 38'.split()

res = map(int, data)
print(res)
res = where(lambda x: not x % 2, res)
print(res)
res = list(map(lambda x: (x, x**2), res))
print(res) """

##ex010-------------------------------------------------##

""" data = [x for x in range(10)]
res = list(filter(lambda x: not x % 2, data))
print(res) """

##ex011-------------------------------------------------##

""" data = '1 2 3 5 8 15 23 38'.split()

res = map(int, data)
print(res)
res = filter(lambda x: not x % 2, res)
print(res)
res = list(map(lambda x: (x, x**2), res))
print(res) """

##ex012-------------------------------------------------##

""" users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]
salary=[111,222,333]
data = zip(users, ids)
print(data)
data = list(zip(users, ids))
print(data)
data = list(zip(users, ids, salary))
print(data) """

##ex013-------------------------------------------------##

users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]
salary=[111,222,333]
data = list(enumerate(users))
print(data)
data = list(enumerate(ids))
print(data)



