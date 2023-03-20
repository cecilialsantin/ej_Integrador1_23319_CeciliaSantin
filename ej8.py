import ej7
from ej7 import Cuenta

class CuentaJoven(Cuenta):
    def __init__(self, cantidad, nombre, dni, edad, bonificacion):
        super().__init__(cantidad, nombre, dni, edad)
        self.__bonificacion = bonificacion
        self.__edad = edad

    def __str__(self):
        return super().__str__(), {self.__bonificacion}
    
    @property
    def bonificacion(self):
        return self.__bonificacion
    
    @bonificacion.setter
    def bonificacion(self,bonificacion):
        self.__bonificacion = bonificacion

    def es_titular_valido(self):
        if int(self.__edad)>18 and int(self.__edad)<25:
            print("Es un usuario válido, puede abrir la cuenta")
        else:
            print("No es un usuario válido")
    
    def mostrar(self):
        if int(self.__edad)>18 and int(self.__edad)<25:
            super().mostrar()
            print(f'Es una cuenta joven y su bonificacion es: {self.__bonificacion}')
        else:
            print(f'El titular no reune los requisitos para abrir una cuenta joven')

    def retirar(self,retiro):
        if int(self.__edad)>18 and int(self.__edad)<25:
            super().retirar(retiro)
        else:
            print(f"No es un usuario valido y por lo tanto no puede retirar de la cuenta joven")


cuentaJoven1=CuentaJoven(100, "Laura", "100333666", 20, 0.05)
cuentaJoven1.es_titular_valido()
cuentaJoven1.mostrar()
cuentaJoven1.retirar(30)

cuentaJoven2=CuentaJoven(40, "Pedro", "25966778", 40, 0.05)
cuentaJoven2.es_titular_valido()
cuentaJoven2.mostrar()
cuentaJoven2.retirar(20)


