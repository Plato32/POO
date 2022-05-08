import csv
from Planahorro import PlanAhorro

class Manejadorplan:
    __listap=[]

    def __init__(self):
        self.__listap=self.cargaplanes()
       
        
        
    def cargaplanes(self):
        lista=[]
        archivo=open("planes.csv")
        reader=csv.reader(archivo, delimiter=";")
        
        for line in reader:
            p=PlanAhorro(line[0],line[1],line[2],line[3])
            lista.append(p)
        archivo.close()
        return(lista)
       


    def actualizar(self):
        for elem in self.__listap:
            print("Código del plan: {} Modelo: {} Versión: {}".format(elem.getcodigo(),elem.getmodelo(),elem.getversion()))
            elem.setnewvalor(input("Ingrese El nuevo Valor para este vehiculo: "))
            print("Nuevo valor es igual a: ",elem.getvalor())
        

    def mostrar_datos_valor(self):
        valor=float(input("Ingrese un valor deseado: "))
        for elem in self.__listap:
            if(elem.getvcuota()<valor):
                print("Código del plan: {} Modelo: {} Versión: {}".format(elem.getcodigo(),elem.getmodelo(),elem.getversion()))
            
    
    def mostrar_monto_licitar(self):
         for elem in self.__listap:
              print("Código del plan: {} Monto que se debe haber pagado para licitar el vehículo: ${:.2f}".format(elem.getcodigo(),elem.monto_licitar()))
    
    def modificar_cant_cuotas_licitar(self):
        cod=input("Ingrese codigo de plan a modificar: ")
        i=0
        print(len(self.__listap))
        while((len(self.__listap)>i)and(self.__listap[i].getcodigo() !=cod)):
            print(i)
            i += 1
        if (i<len(self.__listap)):
            cantidadn=input("Ingrese la nueva cantidad cuotas que debe tener pagas para licitar: ")
            self.__listap[i].setnewcantlic(cantidadn)

            
   
   
        
