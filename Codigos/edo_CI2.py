
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

    # Print latex representation

    ics = {y(x1): y1, y(x).diff(x).subs(x, x2): y2}

    # Aplicamos las condiciones iniciales
    L_edo_4 = eqdiff.subs(ics)

    Y_sol = dsolve(L_edo_4, y(x))

    return Y_sol
