class Proyecto:
    __idProyecto:int
    __titulo:str
    __palabrasClave:str
    __puntos:int

    def __init__(self,id,titulo,palabrasclave,puntos=0):
        self.__idProyecto=id
        self.__titulo=titulo
        self.__palabrasClave=palabrasclave
        self.__puntos=puntos
    
    def __str__(self) -> str:
        return("{}{}{}".format(self.__idProyecto,self.__titulo,self.__palabrasClave))
    
    def getid(self):
        return(self.__idProyecto)
    
    def getitulo(self):
        return(self.__titulo)
    
    def getpuntos(self):
        return(self.__puntos)
    
    def setpuntos(self,pu):
        self.__puntos+=pu
    
    def __gt__(self,otro):
        if(type(otro)==type(self)):
            return(self.__puntos>otro.__puntos)
        else:print("Comparacion erronea")

