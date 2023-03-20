import ej1
from ej1 import maximo_c_divisor

def minimo_c_multiplo(a, b):
    return (a * b) / maximo_c_divisor(a, b)

n1 = int(input ("ingresar el primer número nuevamente: "))
n2 = int(input ("ingresar el segundo número nuevamente: "))

print(f"El Minimo Común Múltiplo entre {n1} y {n2} es", minimo_c_multiplo(n1, n2))




