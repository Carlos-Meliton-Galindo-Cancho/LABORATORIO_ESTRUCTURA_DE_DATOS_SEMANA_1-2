"""
EJERCICIO 2    

VERIFICACIÓN DE NÚMERO PAR O IMPAR:

Solicita un número al usuario y determina si es par o impar.

"""

n= int(input("ingresa un numero: ")) # solicita al usiario un numero, lo convierte a un entero y lo almacena a la variable n

if n%2==0:                       # esta condicional evalúa si el residuo de dividir n entre 2 es igual a cero, y si es verdadero imprime " el numero es par"
    print("el numero es par")
else:                            # si la condicion anterior no se cumple ( es decir es FALSO), imprimira el mensaje que esta despues del else
    print("el numero es impar")



"""
la impresion final sera:

ingresa un numero: 9
el numero es impar

"""














