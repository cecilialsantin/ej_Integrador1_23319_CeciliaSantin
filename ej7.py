import ej6
from ej6 import Persona

class Cuenta:
    def __init__(self, cantidad, nombre, dni, edad):
        self.__cantidad = cantidad
        self.__nombre = nombre
        self.__dni = dni
        self.__edad = edad

    class Titular(Persona):
        def __init__(self, nombre, dni, edad):
            super().__init__(nombre, dni, edad)
    
    def __str__(self):
        return f"La cuenta posee un saldo de: {self.__cantidad} y el Titular es: "
    
    @property
    def cantidad(self):
        return self.__cantidad
    
    @cantidad.setter
    def cantidad(self,cantidad):
        self.__cantidad = cantidad

    @property
    def nombre(self):
        return self.Titular.__nombre
    
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre = self.Titular.nombre

    @property
    def dni(self):
        return self.Titular.__dni
    
    @dni.setter
    def dni(self,dni):
        self.__dni = self.Titular.dni

    @property
    def edad(self):
        return self.Titular.__edad
    
    @edad.setter
    def edad(self,edad):
        self.__edad = self.Titular.edad

    def mostrar(self):
        print(f"El nombre, DNI y Edad de la persona son:")
        print(f"Nombre: {self.__nombre} - DNI: {self.__dni} - EDAD: {self.__edad}")
        print(f"El saldo de la cuenta es:")
        print(f"Saldo: {self.__cantidad}")

    def ingresar(self,ingreso):
        if ingreso>0:
            self.__cantidad+=ingreso
            print(f'Se ingresó dinero y el saldo de la cuenta ahora es: {self.__cantidad}')
        else:
            print(f'El saldo de la cuenta no se incrementó ni disminuyó')

    def retirar(self,retiro):
        self.__cantidad-=retiro
        print(f'Se ha realizado un retiro de dinero y la cantidad en cuenta es: {self.__cantidad}')
       

nueva_cuenta1=Cuenta(25, "Luis", "21665556", 53)
#nueva_cuenta1.mostrar()
#nueva_cuenta1.ingresar(30)
#nueva_cuenta2=Cuenta(10, "Cecilia", "24957711", 35)
#nueva_cuenta2.mostrar()
#nueva_cuenta2.ingresar(50)
#nueva_cuenta2.ingresar(-10)
#nueva_cuenta1.retirar(100)
nueva_cuenta1.mostrar()
nueva_cuenta1.ingresar(20)
nueva_cuenta1.retirar(10)





        
    

