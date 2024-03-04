"""
EJERCICIO 11

ORDENAMIENTO DE LISTA:

Ordena una lista de números ingresados por el usuario de menor a mayor

"""


numeros_ingresados=input("ingrese una lista de numeros separados por espacio: ")    # solicita al usuario que ingrese una lista de números separados por espacios y lo guarda como una cadena de texto en la variable numeros_ingresados

lista_numeros=numeros_ingresados.split()                                # split() se utiliza para dividir la cadena numeros_ingresados en una lista de cadenas utilizando los espacios como separadores

print(sorted(lista_numeros))                                      # sorted() se utiliza para ordenar los elementos de la lista de menor a mayor y el resultado ordenado se imprime utilizando print()



"""
LA IMPRESION FINAL SERA:



"""
















