
from sympy.plotting import plot

from sympy import *


def edo_CI2(ec, x1, y1, x2, y2):

    init_printing(use_latex='mathjax')

    x = symbols('x')

    y = Function('y')
    y1 = Derivative(y(x), x)
    y2 = Derivative(y(x), x, x)

    # Definition
    f = ec
    eqdiff = parse_expr(f)

    # Solution
    sol = dsolve(eqdiff, y(x))

    pprint(sol)

    # Print latex representation

    ics = {y(x1): y1, y(x).diff(x).subs(x, x2): y2}

    # Aplicamos las condiciones iniciales
    L_edo_4 = eqdiff.subs(ics)

    Y_sol = dsolve(L_edo_4, y(x))

    pprint(Y_sol)


edo_CI2("y(x).diff(x, x)-y(x).diff(x)-2*y(x)", 0, 2, 0, 1)
