class PlanAhorro:
    __codigo=str
    __modelo= str
    __version=str
    __valor=float
    __cantidad_cuotas= int(60)
    __cantidad_licitar= int(10) 

    def __init__(self,codigo,modelo,version,valor):
        self.__codigo=codigo
        self.__modelo=modelo
        self.__version=version
        self.__valor=valor
        

    def getcodigo(self):
        return(self.__codigo)
    
    def getmodelo(self):
        return(self.__modelo)
    
    def getversion(self):
        return(self.__version)
        
    def getvalor(self):
        return(self.__valor)
    
    def getcantcuotas(self):
        return(self.__cantidad_cuotas)

    def getvcuota(self):
       
        valorcuota = (float(self.__valor)/int(self.__cantidad_cuotas)) + float(self.__valor) * 0.10
        return(float(valorcuota))

    
    def monto_licitar(self):
        return(self.getvcuota()*self.__cantidad_licitar)

    def setnewvalor(self, newvalor):
        self.__valor=newvalor
    
    def setnewcantlic(self,cl):
        self.__cantidad_licitar= cl
        print(self.__cantidad_licitar)