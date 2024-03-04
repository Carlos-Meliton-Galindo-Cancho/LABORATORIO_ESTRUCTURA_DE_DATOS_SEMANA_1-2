"""
EJERCICIO 10

NÚMEROS DE LA SERIE FIBONACCI:

Genera los primeros 10 números de la serie Fibonacci

"""


def fibonacci(n):                     # se define una función llamada fibonacci que toma un argumento n

    if n==0 or n==1:                   # una condición base para los casos en los que n es 0 o 1
        return n                       # en estos casos la función devolverá el mismo n
    else:
        return fibonacci(n-1) + fibonacci(n-2)          # esta es la parte recursiva de la función y se llama a la función fibonacci() con los argumentos disminuidos en 1 y en 2
n=10                                                 # Se define la variable n con el valor 10
for i in range(n):                           # un bucle for para iterar sobre los primeros n números naturales
    print(fibonacci(i))                      # dentro del bucle se llama a la función fibonacci() con el índice i como argumento y se imprime el resultado























