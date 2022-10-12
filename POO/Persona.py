class Persona:
    def __init__(self,nombre="",apellido="",edad=0,dni=""):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni
        self._apellido = apellido
    # retorna el valor nombre => getter
    #tiene que llamarse igual que el atributo
    @property
    def nombre(self):
        return self.__nombre
    @property
    def edad(self):
        return self.__edad
    #setea un nuevo valor => setter
    @nombre.setter 
    def nombre(self,nuevoNom):
        self.__nombre = nuevoNom
    # define un formato para mostrar la data
    def __str__(self):
        return f"hola soy {self.__nombre+' '+self._apellido}, tengo {self.__edad} años y mi dni es {self.__dni}"
class Alumno(Persona):
    def __init__(self) -> None:
        pass

pablo = Persona('pablo','sandoval',21,'43168585')
print(pablo)
if(pablo.edad >=18):
    print("VIVA EL ALCOHOL 😉")
else:
    print("soy ilegal 😫")