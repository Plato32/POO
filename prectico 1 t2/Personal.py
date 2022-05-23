class Persona:
    __legajo:int
    __dni:str
    __apellido:str
    __nombre=str
    __sueldo:int
    __cobrar:int



    def __init__(self,legajo,dni,apellido,nombre,sueldo,cobrar=0) -> None:
        self.__legajo=legajo
        self.__dni=dni
        self.__apellido=apellido
        self.__nombre=nombre
        self.__sueldo=int(sueldo)
        self.__cobrar=cobrar

    def getape(self):
        return(self.__apellido)

    def getnom(self):
        return(self.__nombre)    

    def getlegajo(self):
        return(int(self.__legajo)) 

    def getsueldo(self):
        return(self.__sueldo)
    
    def getdni(self):
        return(self.__dni)   
    
    def setliquidar(self,monto):
        self.__cobrar=monto
    def getliquidar(self):
        return(self.__cobrar)

    def __gt__(self,otro):
        band=None
        if(type(self)==type(otro)):
            band=self.getape()>otro.getape()
        
        return(band)

    
    def __lt__(self,otro):
        band=None
        if(type(self)==type(otro)):
            band=self.getliquidar()<otro.getliquidar()
        
        return(band)
    
    

        
        



'''La empresa posee un archivo separado por comas, denominado ‘repartidores.csv’, con los datos de los 
repartidores. El archivo almacena: identificador de repartidor, apellido, nombre, teléfono y tipo movilidad 
(‘B’ Bicicleta, ‘M’ Moto, ‘A’ Auto), importe a cobrar por comisión (inicialmente vale 0 para todos los 
repartidores, pues aún no está calculada).'''