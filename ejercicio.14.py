"""
EJERCICIO 14

CALCULO DEL ÁREA DE UN CÍRCULO:

Pide el radio de un círculo al usuario y calcula su área

"""


radio = float(input("Ingresa el radio del círculo: "))            # se solicita al usuario que ingrese el radio del círculo y guarda el valor como un número de punto flotante (float) en la variable radio

pi_aproximado = 3.1416
area = pi_aproximado * (radio ** 2)                                 # se calcula el área del círculo utilizando la fórmula del círculo y el resultado se guarda en la variable area

print(f"El área del círculo con radio {int(radio)} es: {area}")        # se imprime el resultado de la operación



"""
LA IMPRESION FINAL SERA:



"""