class Novedad:
    __legajo:int
    __importe:float
    __concepto:str
    __codigo=str


    def __init__(self,legajo,importe,concepto,codigo) -> None:
        self.__legajo=legajo
        self.__importe=int(importe)
        self.__concepto=concepto
        self.__codigo=codigo
    
    def getlegajo(self):
        return(self.__legajo)

    def getimporte(self):
        return(self.__importe)

    def getconcepto(self):
        return(self.__concepto)

    def getcodigo(self):
        return(self.__codigo)

    

