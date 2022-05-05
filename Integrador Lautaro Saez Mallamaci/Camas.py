class Cama:
    __idCama=""
    __habitacion= ""
    __estado= False
    __nombre_apellido= ""
    __diagnostico=""
    __fecha_internacion= ""
    __fecha_alta= ""

    def __init__(self, idcama, habitacion, estado, nombre_apellido, diagnostico, fechas_internacion, fecha_alta):

        self.__idCama=str(idcama)
        self.__habitacion=str(habitacion)
        self.__estado=bool(estado)
        self.__nombre_apellido=str(nombre_apellido)
        self.__diagnostico=str(diagnostico)
        self.__fecha_internacion=str(fechas_internacion)
        self.__fecha_alta=str(fecha_alta)

    
    def __repr__(self):
        return repr((self.__idCama, self.__habitacion,self.__estado,self.__nombre_apellido,self.__diagnostico,self.__fecha_internacion,self.__fecha_alta))

    def getidC(self):
        return(str(self.__idCama))

    def gethabitacion(self):
        return(str(self.__habitacion))    
    
    def getestado(self):
        return(str(self.__estado))
    
    def getnomyape(self):
        return(self.__nombre_apellido)

    def getdiagnostico(self):
        return(self.__diagnostico)    

    def getfechai(self):
        return(self.__fecha_internacion)
        
    def getfechaA(self):
        return(self.__fecha_alta)

    def setfechaA(self, fecha):
        self.__fecha_alta = fecha
        self.__estado = False
