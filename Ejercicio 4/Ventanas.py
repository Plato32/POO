class Ventana:
    __titulo=""
    __x_si=0
    __y_si=0
    __x_id=0
    __y_id=0
    
    def __init__(self,titulo="Vent",xsi=0,ysi=0,xid=500,yid=500):
        if(xsi<xid)and(xsi<yid):
            self.__titulo=titulo
            self.__x_si=xsi
            self.__y_si=ysi
            self.__x_id=xid
            self.__y_id=yid

        else:
            # print("Error al ingresar los datos")
            exit("Error al ingresar los datos")
    
    def mostrar(self):
        print("Titulo: ",self.__titulo)
        print("Limite Superior Izquierdo: (",self.__x_si,",",self.__y_si,")")
        print("Limite Inferior Derecho: (",self.__x_id,",",self.__y_id,")")

    def getTitulo(self):
        return(self.__titulo)

    def alto(self):
        return(self.__y_id-self.__y_si)

    def ancho(self):
        return(self.__x_id-self.__x_si)
    
    def moverDerecha(self, nv=1):
        if self.__x_si+nv>=0:
            self.__x_si+=nv
        if self.__x_id+nv<=500:
            self.__x_id+=nv    

    def moverIzquierda(self, nv=1):
        if self.__x_id-nv<=500:
           self.__x_id-=nv
        if self.__x_si+nv>=0:
            self.__x_si-=nv    
    
    def bajar(self, nv=1):
        if self.__y_id-nv<=500:
            self.__y_id-=nv
        if self.__y_si-nv>=0:
            self.__y_si-=nv

    
    def subir(self, nv=1):
        if self.__y_id+nv<=500:
            self.__y_id+=nv
        if self.__y_si+nv>=0:
            self.__y_si+=nv

    
    
    
    

