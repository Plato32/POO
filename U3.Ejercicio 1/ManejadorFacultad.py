import csv
from Facultad import Facultad
from Carrera import Carrera

class ManejadorFacultades:
    __lista=[]

    def __init__(self) -> None:
        __lista=self.lecturaArchivos()
    

    def lecturaArchivos(self):
        
        listaf=[]
        archivo = open( 'Facultades.csv')
        reader = csv.reader( archivo, delimiter = ',' )
        fila=next(reader)
        bandera = True
        while bandera:
            #print('Facultad')
            #print(fila)
            
            #print('Carreras:')
            listac=[]
            filaCarrera=next(reader)
            
            while bandera and fila[0]==filaCarrera[0]:
                #print(filaCarrera)
                try:
                    
                    c=Carrera(filaCarrera[1],filaCarrera[2],filaCarrera[3],filaCarrera[3],filaCarrera[4])
                    filaCarrera=next(reader)
                    listac.append(c)

                except StopIteration:
                    bandera=False
            f=Facultad(fila[0],fila[1],fila[2],fila[3],fila[4],listac)
            listaf.append(f)  
            fila=filaCarrera
        archivo.close()
        #print(len(listaf))
        
        '''for elem in listaf:

            print(elem)
            print(elem.muestracarre())'''