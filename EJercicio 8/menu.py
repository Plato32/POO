class Menu:
    __op=int
    __listac=[]

    def __init__(self,list) -> None:
        self.__op=-1
        self.__listac=list
        print(self.__listac)

    def menuop(self):
         
        while(self.__op!=0):
            print("-----------------------------------MENU----------------------------------")
            self.__op=int(input("Ingrese 1 para unir dos conjuntos\nIngrese 2 para la interseccion de dos conjuntos\nIngrese 3 para comparar 2 conjuntos\nIngrese 0 para finalizar la ejecucion\n"))
            if(1==self.__op):
                self.opcion1()
            elif(2==self.__op):
                self.opcion2()
            elif(3==self.__op):
                self.opcion3()
            elif(self.__op==0):
                print('Opcion de salida seleccionada.')
            else:print('Opcion incorrecta seleccionada.') 
            print("")
        print('>>>Finalizando ejecucion.')
    
    def opcion1(self):
        print("El conjunto {} unido con el conjunto {} da como resultado:{}".format(self.__listac[0].getconj(),self.__listac[1].getconj(),self.__listac[0]+self.__listac[1]))

    
    def opcion2(self):
        print("El conjunto {} menos el conjunto {} da como resultado:{}".format(self.__listac[0].getconj(),self.__listac[1].getconj(),self.__listac[0]-self.__listac[1]))
 
    def opcion3(self):
        if(self.__listac[0]==self.__listac[2]):
            print("El conjunto {} y {} son iguales".format(self.__listac[0].getconj(),self.__listac[2].getconj()))
        else:print("El conjunto {} y {} son diferentes".format(self.__listac[0].getconj(),self.__listac[2].getconj()))
       