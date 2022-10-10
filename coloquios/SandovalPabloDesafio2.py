import string
def validar(password):
    if(len(password)>=8 and len(password)<=16):
        hayMayuscula = False
        hayMinuscula = False
        hayCaracterNumerico = False
        for i in range(len(password)):
            if(password[i] in string.ascii_uppercase):
                hayMayuscula = True
            elif(password[i] in string.ascii_lowercase):
                hayMinuscula = True
            elif(password[i].isdigit()):
                hayCaracterNumerico = True
            if(hayMinuscula and hayCaracterNumerico and hayMayuscula):
                return True
    else:
        return False
        

def solicitud():
    mail = input("ingrese correo electronico:")
    password = input("ingrese contraseña")
    if(validar(password)):
        print("Registro Exitoso!")
    else:
        print("ERROR: Contraseña inapropiada")

def main():
    print("Bienvenido a mil programadores! Por favor complete los siguientes datos")
    solicitud()
main()