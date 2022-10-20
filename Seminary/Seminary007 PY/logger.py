def log_expr(a):
    with open('file.txt','w') as f:
        f.write(a)

def log_ans(a):
    with open('file.txt','a') as f:
        f.write(f'={str(a)}')