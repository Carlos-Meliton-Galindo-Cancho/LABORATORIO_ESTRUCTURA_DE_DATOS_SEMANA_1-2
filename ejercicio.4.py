"""
EJERCICIO 4 

CALCULADORA DE FACTORIAL:

Crea una función que calcule la factorial de un número.

"""


def factorial(n):           # se define una función llamada factorial que toma un argumento n
    if n==0 or n==1:       # es una condicional que verifica si n es igual a cero o igual a uno
        return 1           # si la condicional anterior se cumple entonces retornara el valor de 1 y se terminará la ejecución de la funcion para ese caso
    else:
        return n * factorial(n-1)       # esta es la parte recursiva de la función que se ejecutará si la condicional anterior no se cumplió

print(factorial(5))            # aquí se llama a la función factorial con el argumento 5 y se imprime el resultado
 


"""
LA IMPRESION FINAL SERA: 120


"""






















