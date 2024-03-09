"""
EJERCICIO 12

PALÍNDROMO:

Verifica si una palabra ingresada por el usuario es un palíndromo

"""


palabra = input("Ingresa una palabra: ")                    # se solicita al usuario que ingrese una palabra y lo guarda como una cadena de texto en la variable palabra

if palabra == palabra[::-1]:                                # comparación para verificar si la palabra ingresada es igual a su inversa
    print(f"'{palabra}' es un palíndromo.")                 # si la palabra ingresada es igual a su inversa se imprime "es un palíndromo"
else:
    print(f"'{palabra}' no es un palíndromo.")              # si la palabra ingresada no es igual a su inversa se imprime "no es un palíndromo"



"""
LA IMPRESION FINAL SERA:

Ingresa una palabra: reconocer
'reconocer' es un palíndromo.

"""
