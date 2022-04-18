import csv


class Email:
    __idcuenta=''
    __dominio=''
    __tipo_dominio=''
    __contraseña=''

    def __init__(self ,idcuenta ,dominio ,tipo_dominio ,contrasena):
        self.__idcuenta = idcuenta
        self.__dominio= dominio
        self.__tipo_dominio = tipo_dominio
        self.__password = contrasena
    
    def retornaemail(self):
        __emailconca=self.__idcuenta + "@" + self.__dominio + "." + self.__tipo_dominio
        print("Estimado {} te enviaremos tus mensajes a la dirección '{}' ".format(self.__idcuenta,__emailconca))
        return(__emailconca)
    
    def cambiacontra(self):
        __a=1
        while(__a==1):
            __ncontra=int(input("Ingrese su contraseña "))
            if (__ncontra==self.__password):
                print("Contraseña correcta, ingrese nueva contraseña ")
                __nuevapass=int(input("Ingrese contraseña nueva "))
                self.__password=__nuevapass
                __a=0
            else:
                print("Contraseña incorrecta ")
    
    def divemail(self,m):
        __cadena=m.split("@")
        self.__idcuenta=__cadena[0]
        print("La id ingresado es {}".format(self.__idcuenta))
        __cadena=__cadena[1].split(".")
        self.__dominio=__cadena[0]
        print("El dominio ingresado es {}".format(self.__dominio))
        self.__tipo_dominio=__cadena[1]
        print("El tipo de dominio ingresado es {}".format(self.__tipo_dominio))

    def busca(self):
        archivo=open("datos.csv")
        reader=csv.reader(archivo)

        for linea in reader:
            cad=str(linea).split("@")
            id=cad[0]
            cad=cad[1].split(".")
            dominio=cad[0]
            tipo_dominio=cad[1]
            e=Email(id,dominio,tipo_dominio,0)
            lista.append(e)
        archivo.close()

        archivo=open("datos.csv")
        reader=csv.reader(archivo)
        idb="['"+input("Ingrese ID para buscar ")

        c=0
        for linea in reader:

            idl=str(linea).split("@")  
            #print(linea)
            #print(idl[0])
            
            if idl[0] == idb:
                c += 1

        #print("Cantidad de personas con ID {}'] es: {}".format(idb,c))
        if c > 0:
            print("El identificador se repite {} ves/ces".format(c))
        else:
            print("El identificador no se repite")
        archivo.close()
        
       
if __name__ == '__main__':

    lista=[]
    id=input("Ingrese ID del usuario ")
    dominion=input("Ingrese dominio ")
    tipo_dom=input("Ingrese tipo dominio ")
    contra=int(input("Ingrese contraseña del usuario "))

    e=Email(id,dominion,tipo_dom,contra)
    lista.append(e)
    
    print(e.retornaemail())
    e.cambiacontra()
    
    mail=input("Ingrese email ")
    e.divemail(mail)

    e.busca()

    