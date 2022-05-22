from edo_F import ed_f
from laplace_simple import laplace_simple
from laplace_inv import laplace_inv

from sympy import *

salir = False
op = 0


def pedirNumeroEntero():

    correcto = False
    num = 0
    while(not correcto):
        try:
            num = int(input("Introduce un numero entero: "))
            correcto = True
        except ValueError:
            print('Error, introduce un numero entero')

    return num


while not salir:
    print('--------------------------------BIENVENIDO A LA CALCULADORA DE ECUAS--------------------------------\n')
    print('Que desea hacer?\n')
    print('1. Resolver una ecuacion diferencial\n')
    print('2. Realizar una transformada de laplace\n')
    print('3. Realizar una transformada de laplace inversa\n')
    print('4. Salir\n')
    op = pedirNumeroEntero()
    if op == 1:
        print('--------------------------------Ecuacion diferencial--------------------------------\n')
        ec = input(
            'Introduzca la ecuacion a resolver por ejemplo 3*x*y(x).diff(x)-(x**2-9)*y(x)+1/x \n')
        print('La solucion para ', ec, 'es: \n')
        ed_f(ec)

    elif op == 2:
        print('--------------------------------Transformada de laplace--------------------------------\n')
        ec = input('Introduzca la ecuacion (exp(-t)*sin(t))\n')
        print('La solucion para ', ec, 'es: \n')
        laplace_simple(ec)
    elif op == 3:
        print("op 3")
        print('--------------------------------Transformada inversa de laplace--------------------------------\n')
        ec = input('Introduzca la ecuacion (((s+1)**3)/(s**4))\n')
        print('La solucion para ', ec, 'es: \n')
        laplace_inv(ec)
    elif op == 4:
        print('Muchas gracias por usar esta calculadora, adios!')
        salir = True
    else:
        print("Introduce un numero entre 1 y 3")
