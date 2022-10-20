import sympy


def evaluate_expr(expr):
    x = sympy.Symbol('x')
    return sympy.solve(expr, x)
