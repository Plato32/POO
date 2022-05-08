from ManejadorPlan import Manejadorplan

class Menu:
    __op=int
    __listas= Manejadorplan

    def __init__(self):
        op=-1
        self.__listas=Manejadorplan()
    
    def menu_opciones(self):
        
        while(self.__op!=0):
            print("-----------------------------------MENU----------------------------------")
            self.__op=int(input('Escoja la opcion deseada: \n1. Actualizar el valor de cada vehiculo. \n2. Mostrar planes con valor menor al ingresado. \n3. Mostrar monto a pagar para licitar un vehiculo.'
                            '\n4. Modificar Cantidad de Cuotas para licitar segun Codigo. \nPrecione 0  para Salir del Programa. \n-------------------------------------------------------------------------\n'))
            if(self.__op==1):
                self.opcion_1()
            elif(self.__op==2):
                self.opcion_2()
            elif(self.__op==3):
                self.opcion_3()
            elif(self.__op==4): 
                self.opcion_4()
            elif(self.__op==0):
                print('Opcion de salida seleccionada.')
            else:print('Opcion incorrecta seleccionada.') 
           
            print("")
        print('>>>Finalizando ejecucion.')


    def opcion_1(self):
        self.__listas.actualizar()
    def opcion_2(self):
        self.__listas.mostrar_datos_valor()
    def opcion_3(self):
        self.__listas.mostrar_monto_licitar()
    def opcion_4(self):
        self.__listas.modificar_cant_cuotas_licitar()   
       
