import matplotlib.pyplot as plt
from sympy import *


def ed_f(ec):
    init_printing(use_latex='mathjax')
    # Damos de alta la variable simbólica x, y la función Y
    x = Symbol('x')
    y = Function('y')

    # Expresamos la ecuacion
  #  sympy.Eq(3*x*y(x).diff(x)-(x**2-9)*y(x)+1/x)

    # Resolviendo la ecuación
    f = parse_expr(ec)
    pprint(dsolve(f))
