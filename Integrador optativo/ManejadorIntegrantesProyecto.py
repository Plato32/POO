import csv
import numpy as np
from numpy import ndarray
from Integrantes import Integrante


class Manejador_Integrantes:
    __arreglo=ndarray

    def __init__(self):
        self.__arreglo=self.cargaarre()
        # print (self.__arreglo[1])
    
    def cargaarre(self):
        listaux=[]

        archivo=open("integrantesProyecto.csv")
        reader=csv.reader(archivo, delimiter=";")
        next(reader)

        for line in reader:
            
            intg=Integrante(line[0],line[1],line[2],line[3],line[4])
            listaux.append(intg)
        arre=np.array(listaux)

        archivo.close
        return arre
    
    def getarre(self):
        return(self.__arreglo)