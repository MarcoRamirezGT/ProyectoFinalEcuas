import matplotlib.pyplot as plt
import sympy


def laplace_transform_derivatives(e):
    """
    Evalua las transformadas de Laplace de derivadas de funciones sin evaluar.
    """
    if isinstance(e, sympy.LaplaceTransform):
        if isinstance(e.args[0], sympy.Derivative):
            d, t, s = e.args
            n = len(d.args) - 1
            return ((s**n) * sympy.LaplaceTransform(d.args[0], t, s) -
                    sum([s**(n-i) * sympy.diff(d.args[0], t, i-1).subs(t, 0)
                         for i in range(1, n+1)]))

    if isinstance(e, (sympy.Add, sympy.Mul)):
        t = type(e)
        return t(*[laplace_transform_derivatives(arg) for arg in e.args])

    return e


sympy.init_printing(use_latex='mathjax')
# Ejemplo de transformada de Laplace
# Defino las incognitas
t = sympy.symbols("t", positive=True)
y = sympy.Function("y")

# Defino la ecuación
f = sympy.parse_expr('(y(t).diff(t, t) + 3*y(t).diff(t) + 2*y(t))')
edo = y(t).diff(t, t) + 3*y(t).diff(t) + 2*y(t)

# simbolos adicionales.
s, Y = sympy.symbols("s, Y", real=True)
L_edo = sympy.laplace_transform(edo, t, s, noconds=True)
sympy.Eq(L_edo)

# Aplicamos la nueva funcion para evaluar las transformadas de Laplace
# de derivadas
L_edo_2 = laplace_transform_derivatives(L_edo)
sympy.Eq(L_edo_2)
# reemplazamos la transfomada de Laplace de y(t) por la incognita Y
# para facilitar la lectura de la ecuación.
L_edo_3 = L_edo_2.subs(sympy.laplace_transform(y(t), t, s), Y)
sympy.Eq(L_edo_3)
# Definimos las condiciones iniciales
ics = {y(0): 2, y(t).diff(t).subs(t, 0): -3}

# Aplicamos las condiciones iniciales
L_edo_4 = L_edo_3.subs(ics)

# Resolvemos la ecuación y arribamos a la Transformada de Laplace
# que es equivalente a nuestra ecuación diferencial
Y_sol = sympy.solve(L_edo_4, Y)

# Por último, calculamos al inversa de la Transformada de Laplace que
# obtuvimos arriba, para obtener la solución de nuestra ecuación diferencial.
y_sol = sympy.inverse_laplace_transform(Y_sol[0], s, t)

r = sympy.pprint(y_sol)
