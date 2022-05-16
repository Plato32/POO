from numpy import diag_indices


class Integrante:
    __idProyecto:int
    __apellidoNombre:str
    __dni:int
    __categoriaInvestigacion:str
    __rol:str

    def __init__(self,id,apellidonombre,dni,categoria,rol):
        self.__idProyecto=id
        self.__apellidoNombre=apellidonombre
        self.__dni=dni
        self.__categoriaInvestigacion=categoria
        self.__rol=rol

    def __str__(self) -> str:
        return("{}{}{}{}{}".format(self.__idProyecto,self.__apellidoNombre,self.__dni,self.__categoriaInvestigacion,self.__rol))
    
    def getid(self):
        return(self.__idProyecto)
    def getrol(self):
        return(self.__rol)
    def getnivel(self):
        return(self.__categoriaInvestigacion)    