def write_data(a):
    with open('db.txt', 'a') as f:
        f.write(f'{a}')
    print(f'save\n')


def read_data():
    print(f'load\n')
    with open('db.txt', 'r') as f:
        return f.read()


""" def rewrite_data(file, old_str, new_str):
    with open(file, 'r') as f1, open('%s.bak' % file, 'w') as f2:
        for line in f1:
            if old_str in line:
                line = line.replace(old_str, new_str)
            f2.write(line)
    os.remove(file)
    os.rename('%s.bak' % file, file)
    print('ok') """


def rewrite_data(file, old_str, new_str):
    with open(file, 'r') as f:
        old_data = f.read()

    new_data = old_data.replace(old_str, new_str)

    with open(file, 'w') as f:
        f.write(new_data)
    print(f'ok\n')
