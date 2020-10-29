'''def evaluaEdad(edad):

    if edad<0:
        raise TypeError("Edad negativa")

    if edad<20:
        return "Eres muy joven"
    elif edad<40:
        return "Eres joven"
    elif edad<65:
        return "Eres viejo"
    elif edad<100:
        return "Cuidate"

print(evaluaEdad(18))'''

import math

def calcularRaiz(num1):
    if num1<0:
        raise ValueError("No puede ser negativo")
    else:
        return math.sqrt(num1)
op1=(int(input("Introduce un numero: ")))

try:
    print(calcularRaiz(op1))
except ValueError as ErrorDeNegativo:
    print(ErrorDeNegativo)
    
print("Programa terminado")