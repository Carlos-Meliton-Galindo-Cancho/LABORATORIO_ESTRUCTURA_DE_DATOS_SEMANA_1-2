"""
EJERCICIO 8

LISTA DE CUADRADOS:

Crea una lista de los cuadrados de los primeros 10 números naturales

"""


def cuadrados(n):                 # se define una función llamada cuadrados que toma un argumento n
    lista=[]                      # se inicializa una lista vacía llamada (lista) para almacenar los cuadrados de los números naturales
    for i in range(1, n+1):       # se utiliza un bucle for para iterar sobre los primeros n números naturales
        lista.append(i**2)          # se calcula el cuadrado de cada número i y se agrega a la lista lista utilizando el método append()
    return lista                 # una vez completado el bucle la función devuelve la lista (lista)

n=10                               # se define la variable n con el valor 10
print(cuadrados(n))                # se llama a la función cuadrados() con n como argumento y se imprime el resultado















