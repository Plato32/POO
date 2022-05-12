class Carrera:
    __codigo: int
    __nombre:str
 #   __fecha_inicio:str
    __duracion:str
    __titulo:str
    __tipo=str
    def __init__(self,codigo,titulo, nombre,duracion,tipo):
        self.__codigo=codigo
        self.__nombre=nombre
        self.__titulo=titulo
        #self.__fecha_inicio=fecha
        self.__duracion=duracion
        self.__tipo=tipo
    
    def __str__(self) -> str:
        return("{} {} {} {} {}".format(self.__codigo,self.__nombre,self.__titulo,self.__duracion,self.__tipo))




