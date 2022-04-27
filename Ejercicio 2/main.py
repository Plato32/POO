import csv
from viajeros import Viajero_Frecuente
def menu():
    print('--------------MENU--------------')
    print(">>>Para consultar cantidad de millas presione 1")
    print(">>>Para consultar para agregar mas millas a su cuenta presione 2")
    print(">>>Para canjear millas presione 3")
    print(">>>Para salir del menu presione 0")
    m=int(input("Ingrese aqui su opcion seleccionada: "))
    return(m)


if __name__ == '__main__':
    listav= []
    i=0
    band=True

    archivo = open('datos2.csv')
    reader = csv.reader(archivo, delimiter=",")
    next(reader)

    for fila in reader:
        v = Viajero_Frecuente(int(fila[0]), str(fila[1]), str(fila[2]), str(fila[3]), int(fila[4]))
        listav.append(v)
        #print(fila[0],fila[1],fila[2],fila[3],fila[4])
       

    archivo.close()
    
    nvf=int(input("Ingrese Numero de Viajero Frecuente: "))
    while((band) and (len(listav) > i)):
    
        if(int(listav[i].getnumviajero()) == nvf):
                    
            band = False
        else:
            i += 1
    
    if (band==True):
        print("El numero de viajero no se encontro")
    else: 
        print("El numero de viajero fue encontrado")
        print(">>>Abriendo Menu>>>")
        opcion=menu()
        print("")

        while(opcion != 0):
            
            if(opcion == 1):
            
                print("La cantidad de millas del viajero con numero {} es de {} millas".format(nvf,listav[i].cantidadTotaldeMillas()))
            if(opcion == 2):
                nm=int(input('Ingrese la cantidad de millas a sumar  '))
                print("La cantidad de millas anterior es de {}".format(listav[i].cantidadTotaldeMillas()))
                print("La nueva cantidad de millas del viajero con numero {} es de {} millas".format(nvf,listav[i].acumularMillas(nm)))

            if(opcion == 3):
                nmc=int(input('Ingrese la cantidad de millas a canjear  '))
                print("La cantidad de millas anterior es de {}".format(listav[i].cantidadTotaldeMillas()))
                print("La nueva cantidad de millas del viajero con numero {} es de {} millas".format(nvf,listav[i].canjearMillas(nmc)))
            print("")
            opcion=menu()

        print("")
        print('>>>Finalizando ejecucion')
