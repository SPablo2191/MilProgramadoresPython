import random as rd
class Dado():
  def tirar(self):
    resultado = rd.randint(1,6)
    return resultado

  

class Jugador():
  def __init__(self,nombre):
    self.__nombre= nombre
    self.__puntos = 0
    self.__turno = True # Se pone el false si pierde un turno
  @property
  def nombre(self):
    return self.__nombre
  @nombre.setter
  def nombre(self,nuevoNombre):
    self.__nombre = nuevoNombre
  
  @property
  def puntos(self):
    return self.__puntos
  @puntos.setter
  def puntos(self,puntos):
    self.__puntos += puntos
  
  @property
  def turno(self):
    return self.__turno
  @turno.setter
  def turno(self,turno):
    self.__turno = turno
  
  def jugar(self, dados):
    if self.__turno:
      puntos = 0
      for dado in dados:
        puntos+= dado.tirar()
      self.__puntos+=puntos
      if puntos == 6*len(dados):
        self.__turno = False    # si las tiradas de todos los dado dieron 6, pierde un turno
        return 0
      else: 
        return puntos
    else:
      self.__turno= True # En el siguiente turno si jugará
      return -1
  
  

class Juego():
  def __init__(self, jugadas,jugadores=[]):
    self.__jugadas= jugadas
    self.__jugadores= jugadores
    self.__dado= Dado()
    self.__ganador= []

  def jugar(self):
    for jugador in self.__jugadores:
      print(jugador.nombre,end="\t")
    print()
    dados= [self.__dado,self.__dado,self.__dado]
    for jugada in range(self.__jugadas):
      for jugador in self.__jugadores:
        resultado= jugador.jugar(dados)
        if resultado <0:
          print("0",end= "\t")
        elif resultado== 0:
          print(f"{len(dados)*6}",end="\t")
        else:
          print(f"{resultado}",end= "\t")
      print()
  
  def mostrar_posiciones(self):
    self.__jugadores.sort(key= lambda jugador:jugador.puntos,reverse=True)
    print("\n\nPos.\tJugador\t\tPuntos")
    posicion=1
    for jugador in self.__jugadores:
      print(f"{posicion}\t{jugador.nombre}\t\t{jugador.puntos}")
      posicion +=1

j1 = Jugador('jugador 1')
j2 = Jugador('jugador 2')
j3 = Jugador('jugador 3')
j4 = Jugador('jugador 4')
jugadores = [j1,j2,j3,j4]
nuevoJuego = Juego(4,jugadores)
nuevoJuego.jugar()
nuevoJuego.mostrar_posiciones()
    