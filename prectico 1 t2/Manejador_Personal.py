import csv
from ctypes import resize
import numpy as np
from numpy import ndarray
from Personal import Persona

class ManejadorPersonal:
    __arrayp=ndarray
    

    def __init__(self):
        self.__arrayp=np.empty(0, dtype=Persona)
        
    def Agregarpedidos(self):
            archivo = open('personal.csv')
            reader = csv.reader(archivo, delimiter=";")
            next(reader)
            for fila in reader:
                pe= Persona(int(fila[0]), str(fila[1]), str(fila[2]), str(fila[3]), float(fila[4]))
                self.__arrayp=np.append(self.__arrayp,pe)
            archivo.close()
            # print(self.__arrayp)
    
    
    def muestralista(self,list):
        # for nom in self.__arrayp:
        #     print(nom.getape())
        self.__arrayp=np.sort(self.__arrayp)
        # print("******************")
        # for nom in self.__arrayp:
        #     print(nom.getape())
        for per in self.__arrayp:
            acum=0
            print("")
            print("Apellido:{} Nombre:{}\nDNI:{}\nSueldo Basico: ${}".format(per.getape(),per.getnom(),per.getdni(),per.getsueldo()))
            acum=per.getsueldo()
            print("")
            print("Codigo    Concepto    Importe")
            for nov in list:
                if(nov.getlegajo()==per.getlegajo()):
                    if(nov.getcodigo()=="A"):
                        acum+=nov.getimporte()
                    else: acum-=nov.getimporte()
                    # print("%1s %10s $ %8i"%nov.getcodigo(), % nov.getconcepto(),% nov.getimporte())
                    print("{}    {}    ${}".format(nov.getcodigo(),nov.getconcepto(),nov.getimporte()))
            print("Total a cobrar ${}".format(acum))
            per.setliquidar(acum)
        print("")

    
    def getarray(self):
        return(self.__arrayp)
    
    '''def __init__(self, dimension=0):
        if type(dimension)==int:
            self.__dimension=dimension
            self.__cantidad=0
            self.__incremento=1
            self.__arrayp=np.empty(self.__dimension, dtype=Persona)
        else:
            print("Dimension incorrecta")

    def Agregarpedidos(self):
            archivo = open('personal.csv')
            reader = csv.reader(archivo, delimiter=";")
            next(reader)
            for fila in reader:
                pe= Persona(int(fila[0]), str(fila[1]), str(fila[2]), str(fila[3]), float(fila[4]))
                self.__arrayp=np.append(self.__arrayp,pe)
                # if self.__cantidad==self.__dimension:
                #     self.__dimension+=self.__incremento
                #     self.__arrayp.resize(self.__dimension)
                #     self.__arrayp[self.__cantidad]=pe
                #     self.__cantidad+=1
            archivo.close()
            print(self.__arrayp)'''

    def mostrarmenor(self):
        list=[]
        list=self.__arrayp
        menor=max(list)
        print("El suledo meno pertenece a {} {} con u sueldo de ${}".format(menor.getape(),menor.getnom(),menor.getliquidar()))
            
            # print("Apellido:{} Nombre:{} Comision:{} \n".format(el.getape(),el.getnom(),el.getcomision()))
                    
