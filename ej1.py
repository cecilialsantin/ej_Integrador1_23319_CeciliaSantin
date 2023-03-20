def maximo_c_divisor(a, b):
    resto = 0
    while b>0:
        resto = b
        b = a%b
        a = resto
    return a

n1 = int(input ("ingresar un número: "))
n2 = int(input ("ingresar otro número: "))

print(f"El Máximo Común Divisor entre {n1} y {n2} es", maximo_c_divisor(n1, n2))
