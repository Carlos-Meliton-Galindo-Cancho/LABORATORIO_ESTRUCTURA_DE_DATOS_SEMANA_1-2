"""
EJERCICIO 13

GENERADOR DE TABLAS DE MULTIPLICAR:

Crea un programa que genere la tabla de multiplicar de un número ingresado por el usuario

"""


numero = int(input("Ingresa un número para generar su tabla de multiplicar: "))      # se solicita al usuario que ingrese un número y lo guarda como un entero en la variable numero

for i in range(0, 13):                                                            # bucle for que iterará sobre los números del 0 al 12 
    multiplicacion = numero * i                                                   # en cada iteración del bucle se calcula el resultado de la multiplicación del número ingresado (numero) por (i) y el resultado se guarda en la variable multiplicacion
    print(f"{numero} x {i} = {multiplicacion}")                                # en cada iteración del bucle se imprime una línea de la tabla de multiplicar



"""
LA IMPRESION FINAL SERA:



"""



