"""
EJERCICIO 13

GENERADOR DE TABLAS DE MULTIPLICAR:

Crea un programa que genere la tabla de multiplicar de un número ingresado por el usuario

"""


numero = int(input("Ingresa un número para generar su tabla de multiplicar: "))      # se solicita al usuario que ingrese un número y lo guarda como un entero en la variable numero

for i in range(0, 13):                                                               # bucle for que iterará sobre los números del 0 al 12 
    multiplicacion = numero * i                                                      # en cada iteración del bucle se calcula el resultado de la multiplicación del número ingresado (numero) por (i) y el resultado se guarda en la variable multiplicacion
    print(f"{numero} x {i} = {multiplicacion}")                                      # en cada iteración del bucle se imprime una línea de la tabla de multiplicar



"""
LA IMPRESION FINAL SERA:

Ingresa un número para generar su tabla de multiplicar: 9
9 x 0 = 0
9 x 1 = 9
9 x 2 = 18
9 x 3 = 27
9 x 4 = 36
9 x 5 = 45
9 x 6 = 54
9 x 7 = 63
9 x 8 = 72
9 x 9 = 81
9 x 10 = 90
9 x 11 = 99
9 x 12 = 108

"""



