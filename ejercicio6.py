"""
EJERCICIO 6

INVERSIÓN DE CADENA:

Toma una cadena de texto y muestra su inversión.

"""


def invertir_cadena(cadena):       # se define una función llamada invertir_cadena que toma un argumento cadena
    
    return cadena[::-1]       # se utiliza una técnica llamada "slicing" para invertir la cadena

cadena_ingresada = input("Ingrese una cadena de texto: ")   # se solicita al usuario que ingrese una cadena de texto y guarda este valor en la variable cadena_ingresada

print(invertir_cadena(cadena_ingresada))   # se llama a la función invertir_cadena() pasando la cadena ingresada por el usuario como argumento




























