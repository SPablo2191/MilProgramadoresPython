class Persona:
    def __init__(self,nombre,apellido):
        self.__nombre = nombre
        self._apellido = apellido
    # retorna el valor nombre => getter
    @property
    def nombre(self):
        return self.__nombre
    #setea un nuevo valor => setter
    @nombre.setter 
    def nombre(self,nuevoNom):
        self.__nombre = nuevoNom
    # define un formato para mostrar la data
    def __str__(self):
        return self.__nombre+' '+self._apellido
class Alumno(Persona):
    def __init__(self) -> None:
        pass

pablo = Persona('pablo','sandoval')
print(pablo)