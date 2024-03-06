"""
EJERCICIO 7

SUMA DE NÚMEROS PARES:

Calcula la suma de los números pares en un rango especificado por el usuario

"""

inicio=int(input("donde iniciara: "))   # solicita al usuario que ingrese el punto de inicio del rango y guarda este valor como un número entero en la variable inicio
final=int(input("donde acabara: "))     # solicita al usuario que ingrese el punto final del rango y guarda este valor como un número entero en la variable final


def suma_numeros_pares(inicio, final):   # se define una función llamada suma_numeros_pares que toma dos argumentos (inicio y final)
    suma=0                               # se inicializa una variable suma con el valor cero, esta variable se usará para almacenar la suma de los números pares dentro del rango
    for i in range(inicio, final+1):     # se utiliza un bucle for para iterar sobre cada número en el rango
        if i%2==0:                       # se verifica si el número i es par, es decir, si el residuo de la división de i entre 2 es igual a cero
            suma+=i                     # si i es par se suma a la variable
    return suma              # una vez terminado el bucle se retornara la variable suma

print(suma_numeros_pares(inicio, final))   # finalmente, se llama a la función suma_numeros_pares() con los valores de inicio y final ingresados por el usuario



"""
LA IMPRESION FINAL SERA:

donde iniciara: 10
donde acabara: 100
2530

"""



















