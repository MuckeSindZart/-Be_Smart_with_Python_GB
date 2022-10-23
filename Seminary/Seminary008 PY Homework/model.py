def menu():
    print('Выберите режимы работы:')
    print('1. Внесение данных')
    print('2. Поиск данных')
    print('3. Вывод данных')
    print('4. Редактирование')
    print('0. Выход\n')

    menu_select = int(input('=> '))
    return menu_select


def new_input():
    print('Введите данные сотрудника:')

    id = input('ID => ')
    soname = input('Фамилия => ')
    name = input('Имя => ')
    telephone = input('Номер телефона => ')
    beruf = input('Должность => ')
    cost = input('Заработная плата => ')

    data = f'{id}||{soname}||{name}||{telephone}||{beruf}||{cost}\n'
    return data


def search(f):
    search = input('Введите данные для поиска: ')
    data = list(filter(lambda i: search in i, f.split('\n')))
    result = '\n'.join(data)
    return result


def edit(s):
    value = list(filter(lambda i: '||' not in i, s.split('||')))
    print(f'Выберите строку для редактирования.')
    print(f'1)ID:\t\t{value[0]}')
    print(f'2)Фамилия:\t{value[1]}')
    print(f'3)Имя:\t\t{value[2]}')
    print(f'4)Телефона:\t{value[3]}')
    print(f'5)Должность:\t{value[4]}')
    print(f'6)Зарплата:\t{value[5]}')
    print(f'0)Выход:')
    
    select = int(input('=> '))
    print(f'Текущее значение: {value[select-1]}')
    new_value = input('Новое значение => ')
    value[select-1] = f'{new_value}'
    new_data = '||'.join(value)
    return new_data
