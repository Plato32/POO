import csv
from viajeros import Viajero_Frecuente
from Manejadorviajero import ManejadorViajero


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
    archivo.close()
    
    m=ManejadorViajero(listav)
    m.mayormillas()
    m.acumular()
    m.canjear()

 



'''
Sobrecarga por derecha (reverse operators)


Dada la clase ViajeroFrecuente definida en el ejercicio 2 con las 
sobrecargas de operadores solicitadas en el ejercicio 6, resolver lo siguiente:

1-    Comparar las cantidad de millas acumuladas de un viajero frecuente con un valor entero 
a través de la sobrecarga del operador igual (== o __eq__). 
Por ejemplo, sea v una instancia de la clase ViajeroFrecuente, debe ser posible realizar tanto v ==  100 como 100 == v.

2-    Acumular millas se pueda resolver de la siguiente forma:
 sea v una instancia de la clase ViajeroFrecuente, 
 debe ser posible realizar v =  100 + v.

3-    Canjear millas se pueda resolver de la siguiente forma: 
sea v una instancia de la clase ViajeroFrecuente, 
debe ser posible realizar v =  100 - v.'''