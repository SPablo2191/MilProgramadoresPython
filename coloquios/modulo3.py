# Diccionario
# pregunta 1
def pregunta1():
    dic = {"nombre": "pablo", "numero": 4210132}
    print(dic.keys())  # --> retorna una lista
    print(dic.values())  # --> retorna una lista
    x = dic.items()
    print(x)  # --> retorna una tupla

# pregunta 2:


def pregunta2():
    cadena = "Les traigo paz."
    print(cadena[-7])
    print(cadena[8])


# pregunta 3:
def pregunta3(num):
    return num % 2 == 0
    # print(“FIN”) => el return funciona como un "break", osea que pasado el retorno, las siguientes lineas no se leeran

# pregunta 4:


def pregunta4():
    # => con el el end string vacio estas diciendo que esta salida...
    print("Hola", end="")
    x = 10 + 1
    # y la siguiente saldran sobre la misma linea sin espacio entre ellas =>concatenadas
    print("mundo")


def pregunta5():
    d = {1: "a", 2: "b", 3: "c", 4: "d"}
    # esto es un operador logico, evaluas si los terminos coinciden o no => siempre te tirara False
    print("f" == d.values())
    # este va un paso mas viendo si en los distintos valores del diccionario esta "f"
    print("f" in d.values())


def pregunta6():
    x = 1
    return eval('x+1')


def pregunta8():
    tup1 = (1, 2, 3)
    tup2 = (4, 5, 6)
    iterador = zip(tup1, tup2)  # zip() devuelve un iterador
    print(tuple(iterador))


def pregunta9():
    lista = [1, 2, 3, 4, 3]
    print(lista.pop())
    print(lista)


def pregunta10():
    alumno = ("arthur@gmail.com", "Arturo", "Medina", 18)
    print(alumno[0], alumno[1])
    print(alumno[-4:-2]) # retorna la tupla, no me parece muy fino pero si acota lo que tenes de la tupla original a los valores solicitados
    print(alumno[-4], alumno[-3])



