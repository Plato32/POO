import csv
import numpy as np
from numpy import ndarray
from datetime import datetime
from Camas import Cama



class Manejadorcamas:
    __arre=ndarray

    def __init__(self):
        self.__arre=self.cargac()
        # print(self.__arre)

    def cargac(self):
        listac=[]
        archivo = open('camas.csv')
        reader = csv.reader(archivo, delimiter=";")
        next(reader)

        for fila in reader:
        
            ca = Cama(str(fila[0]), str(fila[1]), str(fila[2]), str(fila[3]), str(fila[4]), str(fila[5]), str(fila[6])) 
            listac.append(ca)
            # print(fila[5])

        archivo.close()
        
        arrec=np.array(listac)

        return(arrec)
        
    def buscaAyN(self,AN):
        i=0
        band=True
        ib=-1
        while i<len(self.__arre) and band:
            if(self.__arre[i].getnomyape()==AN):
                ib=i
                band=False
            i+=1
        
        return (ib)

    def getdatos(self,i,AN):
        # fa=input("Ingrese fecha del alta siguiendo el siguiente formato 'dd/mm/aaaa': ")
        fa=datetime.today().strftime('%d/%m/%Y')
        self.__arre[i].setfechaA(fa)
        bandera=-1
        if(self.__arre[i].getnomyape()==AN):
            bandera=self.__arre[i].getidC()
            print("  Paciente: {}  Cama: {}  Habitacion: {}".format(self.__arre[i].getnomyape(),self.__arre[i].getidC(),self.__arre[i].gethabitacion()))
            print("  Diagnostico: {}  Fecha de internacion: {}".format(self.__arre[i].getdiagnostico(),self.__arre[i].getfechai()))
            print("  Fecha de Alta: {}".format(self.__arre[i].getfechaA()))
            print("")
        else:
            print("El paciente no se encontro")
        return(bandera)
        
    def getdiagnostico(self,diag):
        
        for element in self.__arre:
            if((diag==str(element.getdiagnostico()))and(str(element.getestado())=="True")):
        
                print("Paciente: {}  Cama: {}  Habitacion: {}".format(element.getnomyape(),element.getidC(),element.gethabitacion()))
                print("Diagnostico: {}  Fecha de internacion: {}".format(element.getdiagnostico(),element.getfechai()))  
                print("")

       
       