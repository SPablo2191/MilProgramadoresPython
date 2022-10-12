class Libro:
    def __init__(self,titulo,autor,cantEjemplares,cantEjemplaresPrestados=0):
        self.__titulo = titulo
        self.__autor = autor
        self.__cantEjemplares = cantEjemplares
        self.__cantEjemplaresPrestados = cantEjemplaresPrestados
    @property
    def cantEjemplaresPrestados(self):
        return self.__cantEjemplaresPrestados
    @cantEjemplaresPrestados.setter
    def cantEjemplaresPrestados(self,valor):
        self.__cantEjemplaresPrestados = self.__cantEjemplaresPrestados + valor
    def prestar(self):
        if(self.__cantEjemplares!= self.__cantEjemplaresPrestados):
            self.cantEjemplaresPrestados(1)
            print("El prestamo se realizo con exito!")
        else:
            print("no se puede realizar el prestamo")
    def devolver(self):
        if(self.__cantEjemplaresPrestados>0):
            self.__cantEjemplaresPrestados-=1
            print("La devolucion se realizo con exito!")
        else:
            print("Devolucion denegada")
    def __str__(self):
        return f"{self.__titulo} / {self.__autor} / {self.__cantEjemplares} / {self.__cantEjemplaresPrestados}"
librin = Libro("sandokan","gonzalo Oropeza",3)
print(librin)
librin.prestar()
print(librin)
librin.prestar()
librin.prestar()
librin.prestar()
print(librin)
librin.devolver()
librin.devolver()
librin.devolver()
librin.devolver()
print(librin)