import csv
# with open("contactos.csv", "w", newline="\n") as csvfile:
#     lector = csv.reader(csvfile, delimiter=",")
#     for nombre, profesion, correo in lector:
#         print(nombre, profesion, correo)

def minMaxAvgCotiz(fichero):
    with open(fichero, "r", newline="\n") as csvfile:
        lector = csv.reader(csvfile, delimiter=";")
        nuevoFichero = [
        ('minimo','maximo','media')
    ]
        j = 0
        vec1 = []
        mini1 =  999999
        avg1 = 0
        maxi1 =  0

        vec2 = []
        mini2 =  999999
        avg2 = 0
        maxi2 =  0

        vec3 = []
        mini3 =  999999
        avg3 = 0
        maxi3 =  0

        vec4 = []
        mini4 =  999999
        avg4 = 0
        maxi4 =  0

        vec5 = []
        mini5 =  999999
        avg5 = 0
        maxi5 =  0
        for Nombre,Final,Máximo,Mínimo,Volumen,Efectivo in lector:
            if( j == 0):
                vec1.append(Final)
                vec2.append(Máximo)
                vec3.append(Mínimo)
                vec4.append(Volumen)
                vec5.append(Efectivo)
            else:
                aux1 = float(Final.replace(",", "."))
                mini1 = min(aux1,mini1)
                maxi1 = max(aux1,maxi1)
                avg1 = avg1 + aux1

                aux2 = float(Máximo.replace(",", "."))
                mini2 = min(aux1,mini1)
                maxi2 = max(aux1,maxi1)
                avg2 = avg1 + aux1

                aux3 = float(Mínimo.replace(",", "."))
                mini3 = min(aux3,mini3)
                maxi3 = max(aux3,maxi3)
                avg3 = avg3 + aux3

                aux4 = float(Volumen.replace(".", ""))
                mini4 = min(aux4,mini4)
                maxi4 = max(aux4,maxi4)
                avg4 = avg4 + aux4

                aux5 = float(Efectivo.replace(",", "."))
                mini5 = min(aux5,mini5)
                maxi5 = max(aux5,maxi5)
                avg5 = avg5 + aux5                            
            j = j + 1
        vec1.append(mini1)
        vec1.append(maxi1)
        vec1.append(avg1/j-1)

        vec2.append(mini2)
        vec2.append(maxi2)
        vec2.append(avg2/j-1)

        vec3.append(mini3)
        vec3.append(maxi3)
        vec3.append(avg3/j-1)

        vec4.append(mini4)
        vec4.append(maxi4)
        vec4.append(avg4/j-1)

        vec5.append(mini5)
        vec5.append(maxi5)
        vec5.append(avg5/j-1)

        nuevoFichero.append(tuple(vec1))
        nuevoFichero.append(tuple(vec2))
        nuevoFichero.append(tuple(vec3))
        nuevoFichero.append(tuple(vec4))
        nuevoFichero.append(tuple(vec5))
    return nuevoFichero

def escribir(nuevofichero):
    with open("cotizacion2.csv", "w", newline="\n") as csvfile:
        escritor = csv.writer(csvfile, delimiter=";")
        for linea in nuevofichero:
            escritor.writerow(linea)




def comaPunto(num):
    for i in range(len(num)):
        print(num[i])
        if(num[i] == ','):
            num[i] = '.'
    return float(num)

def Punto(num):
    for i in range(len(num)):
        if(num[i] == ','):
            num[i] = ''
    return num

escribir(minMaxAvgCotiz('D:/uni/mil Programadores/MilProgramadoresPython/coloquios/cotizacion.csv'))