import csv
import numpy as np
from numpy import ndarray
from Novedades import Novedad
from Personal import Persona


class ManejadorNovedades:
    __listan=[]

    def __init__(self,array):
        self.__listan=self.cargap(array)
        # print(len(self.__listan))

    def cargap(self,array):
        listaux=[]
        archivo = open('novedades.csv')
        reader = csv.reader(archivo, delimiter=";")
        next(reader)

        for fila in reader:
            for filaa in array:
                if(filaa.getlegajo()==int(fila[0])):
                    no=Novedad(int(fila[0]), str(fila[1]), str(fila[2]), str(fila[3]))
                    listaux.append(no)

        archivo.close()
        return (listaux)

    def sueldoliquidar(self,le,arr):
        band=True
        
        for per in arr:     
            if int(per.getlegajo())==int(le):
                band=False
                suel=per.getsueldo()
        if band:
            print("No se encontro el legajo")
        else:
            for nov in self.__listan:
                if (int(le)==nov.getlegajo()):
                    if(nov.getcodigo()=="A"):
                        suel+=nov.getimporte()
                    else: suel-=nov.getimporte()
            
            print("El suledoa  liquidar de la persona con legajo:{}  es de {} pesos".format(le,int(suel)))
                    
    
    def getlistan(self):
        return(self.__listan)


   