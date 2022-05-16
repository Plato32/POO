import csv
import numpy as np
from numpy import ndarray
from ManejadorIntegrantesProyecto import Manejador_Integrantes
from numpy import ndarray
from Proyectos import Proyecto

class Manejador_Proyecto:
    __listap=[]
    __arregloi=ndarray

    def __init__(self):
        self.__listap=self.cargalista()
        mi=Manejador_Integrantes()
        self.__arregloi=mi.getarre()
        # print (self.__listap[1])
    
    def cargalista(self):
        listaux=[]
        
        archivo=open("proyectos.csv")
        reader=csv.reader(archivo, delimiter=";")
        next(reader)

        for line in reader:
            
            proy=Proyecto(line[0],line[1],line[2])
            listaux.append(proy)
        archivo.close
        return listaux
    
    def puntuar(self):
        for eleml in self.__listap:
            cont=0
            bandD=False
            bandC=False
            bandeD=False
            bandeC=False
            print("")
            print("Proyecto siendo puntuado:",eleml.getitulo())
            print("")
            for elem in self.__arregloi:
                if (eleml.getid()==elem.getid()):
                    cont+=1
                    if(elem.getrol()=="director"):
                        bandeD=True
                        if(elem.getnivel()=="I")or(elem.getnivel()=="II"):
                            bandD=True
                    if(elem.getrol()=="codirector"):
                        bandeC=True
                        if(elem.getnivel()=="I")or(elem.getnivel()=="II")or(elem.getnivel()=="III"):
                            bandC=True

           
            if(cont>=3):
                eleml.setpuntos(10)
            else:
                print('El Proyecto de titulo debe tener como minimo 3 integrantes.')
                eleml.setpuntos(-20)
            if(bandD):
                eleml.setpuntos(10)              
            else:
                print('El Director del Proyecto debe tener categoria I o II.')
                eleml.setpuntos(-5)
            if(bandC):
                eleml.setpuntos(10)              
            else:
                print('El Codirector del Proyecto debe tener como minimo categoria III')
                eleml.setpuntos(-5)
            if(not(bandeD)):
                print('El Proyecto debe tener un Director.')
                eleml.setpuntos(-10)    
            if(not(bandeC)):
                print('El Proyecto debe tener un Codirector.')
                eleml.setpuntos(-10) 
            print("") 
  

    def comparamuestra(self):
        self.__listap.sort(reverse=True)

        for elem in self.__listap:
            print("")
            print("El proyecto de titulo {} tiene {} puntos".format(elem.getitulo(),elem.getpuntos()))
        # for i in len(self.__listap):
        #     if self.__listap[i]>self.__listap[i+1]:
                       
            
            
            
