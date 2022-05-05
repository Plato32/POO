import csv
import numpy as np
from numpy import ndarray
from Medicamentos import Medicamento


class Manejadormedicamento:
    __listam=[]

    def __init__(self):
        self.__listam=self.cargam()
        

    def cargam(self):
        listame=[]
        archivo = open('medicamentos.csv')
        reader = csv.reader(archivo, delimiter=";")
        next(reader)

        for fila in reader:
        
            me = Medicamento(str(fila[0]), str(fila[1]), str(fila[2]), str(fila[3]), str(fila[4]), str(fila[5]),float(fila[6])) 
            # print(float(fila[6]))
            listame.append(me)

        archivo.close()
        return (listame)

    def buscaid(self,id):
        i=0
        ib=-1
        acum=0
        print("       Medicamento/monodroga               Presentacion             Cantidad       Precio")
         
        for elem in self.__listam:
            # print(elem)
            # print("Elemento seleccionado",elem.getidCa())
            # print("Id a comparar",id)
            if(id==elem.getidCa()):
                acum+=elem.getprecio()
                print("       {}/{}                {}             {}        ${}".format(elem.getnombre(),elem.getmonodroga(),elem.getpresentacion(),elem.getcantidad(),elem.getprecio()))
        print("       Total adeudado:                                                     $", acum)    
                                            
        return (i)

   