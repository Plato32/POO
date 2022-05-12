from Carrera import Carrera

class Facultad:
    __codigo: int
    __nombre:str
    __direccion:str
    __localidad:str
    __telefono:str
    __Carrera: Carrera


    def __init__(self,codigo,nombre,direccion,localidad,telefono):
        self.__codigo=codigo
        self.__nombre=nombre
        self.__direccion=direccion
        self.__localidad=localidad
        self.__telefono=telefono


