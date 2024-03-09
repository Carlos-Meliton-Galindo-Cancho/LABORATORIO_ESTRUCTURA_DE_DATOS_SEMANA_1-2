"""
EJERCICIO 5 

NÚMERO PRIMO:

Verifica si un número ingresado por el usuario es primo o no.

"""



def es_primo(numero):                                                             # se define una función llamada es_primo que toma un argumento numero
    
    if numero < 2:                                                                # condicional para verificar si el numero es menor que dos, ya que los numeros primos son > 1
        return False
    for i in range(2, int(numero**0.5) + 1):                                      # este bucle for itera sobre los números desde 2 hasta la raíz cuadrada del número ingresado más 1.
        if numero % i == 0:
            return False
    return True

numero_ingresado = int(input("Ingrese un número para verificar si es primo: "))   # solicita al usuario que ingrese un número para verificar si es primo y guarda este valor como un entero en la variable numero_ingresado.

if es_primo(numero_ingresado):                                                    # se llama a la función es_primo() con el número ingresado por el usuario. Si devuelve True, significa que el número es primo
    print(f"{numero_ingresado} es un número primo.")
else:                                                                             # si la función es_primo() devuelve False, se ejecuta el bloque de código después del else:
    print(f"{numero_ingresado} no es un número primo.")



"""
LA IMPRESION FINAL SERA:

Ingrese un número para verificar si es primo: 9
9 no es un número primo.

"""














