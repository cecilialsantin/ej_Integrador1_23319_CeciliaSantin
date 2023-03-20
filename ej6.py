class Persona:
    def __init__(self, nombre, dni, edad):
        self.__nombre = nombre   
        self.__dni = dni
        self.__edad = edad

    def __str__(self):
        return f'{self.nombre} {self.dni} {self.edad}'

    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def dni(self):    
        assert len(self.__dni) > 3, 'Debe asignar un DNI, controle que sea escrito correctamente'
        return self.__dni
    
    @property
    def edad(self):
        return self.__edad

    @nombre.setter
    def nombre(self,nombre):
        self.__nombre = nombre

    @dni.setter
    def dni(self,dni):
        self.__dni = dni

    @edad.setter
    def edad(self,edad):
        self.__edad = edad

    def mostrar(self):
        print(f"El nombre, DNI y Edad de la persona son:")
        print(f"Nombre: {self.__nombre} - DNI: {self.__dni} - EDAD: {self.__edad}")
    
    def es_mayor_edad(self):
        if int(self.__edad)>=18:
            print("La persona es mayor de edad")
        else: print("La persona es menor de edad")
    
    
#nueva_persona1 = Persona("Cecilia", "24957711", 10)
#nueva_persona1.es_mayor_edad()
#nueva_persona1.edad=25
#nueva_persona1.mostrar()