"""
EJERCICIO 15

SUMA DE DÍGITOS:

Toma un número entero y calcula la suma de sus dígitos

"""


numero = 34 
cadena=str(numero)                                           # Se convierte el número entero en una cadena de texto

suma_digitos = 0                                             # se inicializa la variable suma_digitos con el valor cero

for digito in cadena:                                        # bucle for que itera sobre cada carácter en la cadena (cadena)
    suma_digitos += int(digito)                              # en cada iteración el dígito actual (que está en forma de cadena) se convierte a entero utilizando int() y se suma al valor actual de suma_digitos

print(f"La suma de los dígitos es: {suma_digitos}")          # se imprime el resultado



"""
LA IMPRESION FINAL SERA:

La suma de los dígitos es: 7

"""

