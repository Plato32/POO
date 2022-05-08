from __future__ import annotations


class Viajero_Frecuente:
    __numviajero=''
    __dni=''
    __nombre=''
    __apellido=''
    __millas_acum=0

    def __init__(self ,numviajer ,dnii ,nomb ,apellid, millas_a):
        self.__numviajero = numviajer
        self.__dni= dnii
        self.__nombre = nomb
        self.__apellido = apellid
        self.__millas_acum = int(millas_a)
       
        #print(self.__nombre)
    
    def cantidadTotaldeMillas(self):
        return(self.__millas_acum)

    def acumularMillas(self, nuevacant):
        self.__millas_acum+=nuevacant
        return(int(self.__millas_acum))

    def canjearMillas(self,canjm):
        if (self.__millas_acum >= canjm):
            self.__millas_acum-=canjm
        else: print("La cantidad de millas acumuladas es insuficiente")
        return(int(self.__millas_acum))
    
    def getnumviajero(self):
        return(int(self.__numviajero))
    
    def getnombrecompleto(self):
        return(self.__nombre+" "+self.__apellido)
    
    def __gt__ (self, otro):
        if (type(otro)==type(self)):
            return(self.__millas_acum > otro.__millas_acum)
            
        else:
            return("Eror")
    def __add__(self, sumando):
        return(self.acumularMillas(sumando))
    
    def __sub__(self, restando):
        return(self.canjearMillas(restando))

     # return (True)
            # else:
            #     return (False)









    

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
