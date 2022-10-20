import model
import logger

def get_expr():
    return input()


def show_res(a):
    print(a)


expression = get_expr()
logger.log_expr(expression)
answer = model.evaluate_expr(expression)
logger.log_ans(answer)
show_res(answer)
