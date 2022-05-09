from viajeros import Viajero_Frecuente

class ManejadorViajero:
    __listaviaj=[]

    def __init__(self,listavi):
        self.__listaviaj=listavi
        # print(len(self.__listaviaj))
    
    def mayormillas(self):
        mayor=self.__listaviaj[0].cantidadTotaldeMillas()
        print(mayor)

        for elem in self.__listaviaj:
            if elem > mayor:
                mayor=elem
            # if elem.cantidadTotaldeMillas()>mayor:
            #     mayot=elem.cantidadTotaldeMillas()
            
        print("Los viajeros con mayor cantidad de millas acumuladas son:")
        for elem in self.__listaviaj:
            if mayor.cantidadTotaldeMillas()==elem:
                
                print("Numero Viajero: {}  Nombre: {}  Cantidad de Millas: {}".format(elem.getnumviajero(), elem.getnombrecompleto(), elem.cantidadTotaldeMillas()))

    def acumular(self):
        print("")
        nm=int(input('Ingrese la cantidad de millas a sumar a todos los viajeros:  '))
        print("")
        for elem in self.__listaviaj:
                print("La cantidad de millas anterior es de {}".format(elem.cantidadTotaldeMillas()))
                print("La nueva cantidad de millas es de {} millas".format(nm+elem)) 
        print("") 

    def canjear(self):
        print("")
        nm=int(input('Ingrese la cantidad de millas a canjear en todos los viajeros:  '))
        print("")
        for elem in self.__listaviaj:
                print("La cantidad de millas anterior es de {}".format(elem.cantidadTotaldeMillas()))
                print("La nueva cantidad de millas es de {} millas".format(nm-elem))     
        print("")