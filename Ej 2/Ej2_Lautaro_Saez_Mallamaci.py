from posixpath import split
import string
import csv


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
        print(self.__nombre)

    

if __name__ == '__main__':
    
    archivo = open('datos 2.csv')
    reader = csv.reader(archivo)

    for fila in reader:
        cad=str(fila).split(",")
        numvi = cad[0]
        Dni=cad[1]
        Nombre=cad[2]
        Apellido=cad[3]
        Millas_acum=cad[4]
        e=Viajero_Frecuente(numvi,Dni,Nombre,Apellido,Millas_acum)
    archivo.close()
    

    ''''lista=[]
    numvi=input("Ingrese numero del viajero ")
    Dni=string(input("Ingrese dni del viajero "))
    Nombre=input("Ingrese nombre del viajero ")
    Apellido=input("Ingrese apellido del viajero")
    Millas_acum=input("Ingrese cant millas ")
    '''
    

'''
Listas

En una aerolínea ofrece una promoción a sus viajeros frecuentes 
que consiste en acumular puntos por los viajes que realizan, 
pudiendo luego recibir beneficios a través del canje de puntos.

Usted trabaja en el área de sistemas de la aerolínea y le han solicitado 
la implementación de un sistema capaz de gestionar la promoción. 
Respetando el siguiente diseño de clase:
Atributos: número de viajero, DNI, nombre, apellido y millas acumuladas.
metodos:
a- El constructor.
b- “cantidadTotaldeMillas”, retorna la cantidad de millas acumuladas.
c- “acumularMillas”, recibe como parámetro la cantidad de millas recorridas, 
las suma en el atributo correspondiente y retorna el valor del atributo actualizado.
d- “canjearMillas”, recibe como parámetro la cantidad de millas a canjear. 
Para utilizar las millas debe verificarse que la cantidad a canjear sea menor o igual 
a la cantidad de millas acumuladas, caso contrario mostrar un mensaje de error en la operación. 
Retorna el valor de la cantidad de millas acumuladas.

Implemente un programa que:

1- Leer de un archivo separado por comas los datos para crear instancias de la clase ViajeroFrecuente, 
y almacenarlas en una lista.

2- Lea por teclado un número de viajero frecuente y presente un menú con las siguientes opciones:

a- Consultar Cantidad de Millas.

b- Acumular Millas.

c- Canjear Millas.

3- Represente el almacenamiento en memoria para la lista cargada con 4 viajeros.'''

    
