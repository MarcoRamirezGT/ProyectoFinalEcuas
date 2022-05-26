import sympy as sym
from sympy.abc import s, t, x, y, z
from sympy.integrals import laplace_transform
from sympy.integrals import inverse_laplace_transform
from sympy import *

init_printing(use_latex='mathjax')


def laplace_inv(ec):

    # Laplace transform (t->s)
    f = parse_expr(ec)
    U = inverse_laplace_transform(f, s, t)
    return U
