"""
EJERCICIO 9

CONTADOR DE VOCALES:

Cuenta el número de vocales en una cadena de texto

"""


texto = "Puedes contar el numero"         # se define una cadena de texto llamada texto que contiene la frase donde se contará el número de vocales

contador_vocales = 0                      # se inicializa una variable llamada contador_vocales con el valor cero. Esta variable se utilizará para almacenar el número de vocales encontradas

for caracter in texto:                              # se inicia un bucle for que itera sobre cada carácter en la cadena de texto
    if caracter in "aeiou":                          # se verifica si el carácter está presente en la cadena de texto "aeiou"
        contador_vocales = contador_vocales + 1       # si el carácter es una vocal se incrementa en 1 

print(f"El número de vocales en '{texto}' es: {contador_vocales}")     #  se utiliza una f-string para formatear la cadena de salida



"""
LA IMPRESION FINAL SERA:

El número de vocales en 'Puedes contar el numero' es: 9

"""