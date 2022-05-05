from http.client import PRECONDITION_FAILED


class Medicamento:
    __idCa=""
    __idMedicamento=""
    __nombre=""
    __monodroga=""
    __presentacion=""
    __cantidad_apli=0
    __precio_total=0.0

    def __init__(self,idCa,idMedicamento,nombre,monodroga,presentacion,cantidad_apli,precio_total):
        self.__idCa=idCa
        self.__idMedicamento=idMedicamento
        self.__nombre=nombre
        self.__monodroga=monodroga
        self.__presentacion=presentacion
        self. __cantidad_apli=cantidad_apli
        self.__precio_total=precio_total
    
    def __repr__(self):
        return repr((self.__idCa, self.__idMedicamento,  self.__nombre,self.__monodroga,self.__presentacion,self.__cantidad_apli,self.__precio_total))

    def getidCa(self):
        return(self.__idCa)

    def getidMe(self):
        return(self.__idMedicamento)

    def getnombre(self):
        return(self.__nombre)    
    
    def getmonodroga(self):
        return(self.__monodroga)
    
    def getpresentacion(self):
        return(self.__presentacion)

    def getcantidad(self):
        return(self.__cantidad_apli)    

    def getprecio(self):
        return(self.__precio_total)
        
  
    
    
    
    
    
    
    

'''
A cada paciente internado, se le aplican medicamentos, los datos de los medicamentos se 
almacenan en un archivo “medicamentos.csv”, que guarda la siguiente información: idCama, 
idMedicamento (1 a 100), nombre comercial, monodroga, presentación, cantidad aplicada, 
precio total (este archivo se genera sin un orden particular).
'''