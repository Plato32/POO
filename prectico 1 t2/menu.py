import csv
import numpy as np
from numpy import array, ndarray
from Novedades import Novedad
from Personal import Persona
from Manejador_Novedades import ManejadorNovedades
from Manejador_Personal import ManejadorPersonal


class Menu:
    __op:int

    def __init__(self) -> None:
        self.__op=-1

    def menuopciones(self):
        mp=ManejadorPersonal()
        mp.Agregarpedidos()
        array=mp.getarray()
        mn=ManejadorNovedades(array)
        
        
        while self.__op!=0:
            self.__op=int(input("\nIngrese la opcion a ejecutar\n'1' Dado el numero de legajo de una persona, obtener el sueldo a liquidar\n'2' Listar por orden alfabetico "
                                "\n'3'Mostrar el sueldo mas bajo\n'0' Finalizar ejecucion\n"))

            if (self.__op==1):
                self.opcion1(array,mn)
            elif(self.__op==2):
                self.opcion2(mn,mp)
            elif(self.__op==3):
                self.opcion3(mp)
            elif(self.__op==0):
                print("Finalizando ejecucion")
            else:print("Opcion incorrecta")
            print("")
            
            
    def opcion1(self,array,mn):
        print("")
        leg=input("Ingrese el legajo de una persona:")
        mn.sueldoliquidar(leg,array)

    def opcion2(self,mn,mp):
        lista=mn.getlistan()
        mp.muestralista(lista)

    def opcion3(self,mp):
        mp.mostrarmenor()
    


'''a. Dado el número de legajo de una persona, obtener el sueldo a liquidar (sueldo básico 
más los adicionales, menos los descuentos).
b. Obtener un listado con el siguiente formato (ordenado alfabéticamente por nombre y 
apellido, para efectivizar el ordenamiento, debe sobrecargar el operador __gt__ en la 
clase que corresponda).
cObtener el sueldo a cobrar más bajo de todo el personal, para ello deberá sobrecargar 
el operador __lt__ en la clase que corresponda
'''