
from sympy.plotting import plot

from sympy import *


def edo_CI1(ec, x1, y1):

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

    ics = {y(x1): y1}

    # Aplicamos las condiciones iniciales
    L_edo_4 = eqdiff.subs(ics)

    Y_sol = dsolve(L_edo_4, y(x))

    pprint(Y_sol)


edo_CI1("y(x).diff(x)-", 1, 0.5)
