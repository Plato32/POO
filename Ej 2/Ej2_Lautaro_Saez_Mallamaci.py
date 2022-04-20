import string


class Viajero_Frecuente:
    __numviajero=''
    __dni=''
    __nombre=''
    __apellido=''
    __millas_acum=''


    def __init__(self ,numviajero ,dni ,nombre ,apellido, millas_acum):
        self.__numviajero = numviajero
        self.__dni= dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__millas_acum = millas_acum

if __name__ == '__main__':

    lista=[]
    numvi=input("Ingrese numero del viajero ")
    Dni=string(input("Ingrese dni del viajero "))
    Nombre=input("Ingrese nombre del viajero ")
    Apellido=input("Ingrese apellido del viajero")
    Millas_acum=input("Ingrese cant millas ")

    e=Viajero_Frecuente(numvi,Dni,Nombre,Apellido,Millas_acum)
    