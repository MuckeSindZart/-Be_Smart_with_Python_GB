##ex001-------------------------------------------------##

print('Hello World!')

##ex002-------------------------------------------------##

""" a = 123
b = 1.23
print(f'{a} {type(a)}')
print(f'{b} {type(b)}')

value = 1234
print(value)

s = 'Hello World!'
print(f'{s} {type(s)}')

print(a, '-', b, '-', s)
print('{} - {} - {}'.format(a, b, s))
print('{1} - {2} - {0}'.format(a, b, s))
print(f'{a} - {b} - {s}')


f = True
print(f) """

##ex003-------------------------------------------------##

""" list = [1, 2, 3]
print(list)

listA = ['1', '2', '3', 'hello']
print(listA)

listB = ['1', '2', '3', 'hello', 1, 2, 3, True]
print(listB) """

##ex004-------------------------------------------------##

""" print('Input a:')
a = input()
print('Input b:')
b = input()
print(a, b)
print(f'{a} + {b} = {a+b}')  # '1'+'2' = '12'
print(f'{a} + {b} = {int(a)+int(b)}')  # 1 + 2 = 3
print(f'{a} + {b} = {float(a)+float(b)}')  # 1.1 + 2.1 = 3.2 """

##ex005-------------------------------------------------##
""" +,-,*,/,%,//,** """

""" a = 2
b = 4
c = a**b  # a^b 2**4=16
print(c)

aa = 1.3
bb = 3
cc = aa*bb
print(cc)
print(round(cc,2))

aaa = 3
print(aaa)
aaa += 5
print(aaa)
aaa *= 2
print(aaa) """

##ex006-------------------------------------------------##

""" >,>=,<,<=,==,!=
    not,and,or
is,is not ,in ,not in"""

""" a = 1 < 3 and 5 > 2
print(a)

a = 1 == 2
print(a)

a = 1 != 2
print(a)

aa = 'asd'
bb = 'asd'
print(aa == bb)  # True

aaa = [1, 2, 3]
bbb = [1, 2, 3]
print(aaa == bbb)  # True


f = [1, 2, 3]
print(2 in f)  # True
print(not 2 in f)  # False

is_odd = f[0] % 2 == 0
print(is_odd)  # False """

##ex007-------------------------------------------------##

""" if,elif,else """

""" a = int(input('a='))
b = int(input('b='))
if a > b:
    print(a)
else:
    print(b) """

##ex008-------------------------------------------------##

""" original = 123454
print(original)
inverted = 0
while original != 0:
    inverted = inverted * 10 + (original % 10)
    original//=10
print(inverted) """

##ex009-------------------------------------------------##

""" for i in 1, 2, 3:
    print(i**2)

list = [1, 2, 3]
for i in list:
    print(i)


for i in range(4):
    print(i)

for i in range(1,10,2): 
    print(i)

for i in 'asd - qwe': 
    print(i) """

##ex010-------------------------------------------------##

""" txt = 'Съешь ещё этих мягких французких булок'

print(len(txt))
print('ещё' in txt)
print(txt.isdigit())
print(txt.islower())
print(txt.replace('Съешь', 'cъешь'))
print(txt.islower())
txt = txt.replace('Съешь', 'cъешь')
print(txt.islower())
print(txt[2:5])
print(txt[6:-18]) """

##ex011-------------------------------------------------##

""" rng = range(1, 7)
print(rng)
print(type(rng))
rng = list(rng)
print(type(rng))
print(rng)

numbers = [1, 2, 3, 4, 5]
print(numbers)
numbers[0] = 10
print(numbers)

for i in numbers:
    i *= 2
    print(i) """

##ex012-------------------------------------------------##


def f(x):
    if x == 1:
        return 'int'
    elif x == 2.3:
        return 23
    else:
        return

arg = 2
print(f(arg))
print(type(f(arg)))

