"""Metodo iterativo"""
#def get_int():
   # while True:
        #numero_ingresado = input("Ingresar un numero entero: ")
        #try:
            #valor = int(numero_ingresado)
        #except ValueError:
            #print("El número ingresado no es un numero entero, ingresar otro numero que sea entero")
        #else:
            #return print(f"El numero ingresado - {valor} - es un entero")

#get_int()

"""Metodo recursivo"""

def get_int():
    numero_ingresado = input("Ingresar un numero entero: ")
    try:
        valor = int(numero_ingresado)
    except ValueError:
        print("El número ingresado no es un numero entero, ingresar otro numero que sea entero")
        return get_int()
    else:
        return print(f"El numero ingresado - {valor} - es un entero")


get_int()
