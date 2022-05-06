from Ventanas import Ventana
if __name__ == '__main__':
   
    print('==== Ventana Inicio ====')
    # print("")
    # print("Los valores por defecto son los siguientes:")
    ventanaInicio= Ventana('Inicio')
    ventanaInicio.mostrar()

    # op=int(input("Si quiere modificarlos presione '1', si prefiere mantener ests valores presione  0: "))
    # if op==1:
    #     t=input("Ingrese el titulo para la ventana: ")
    #     Xsi=int(input("Ingrese el valor 'X' del borde superior izquierdo: "))
    #     Ysi=int(input("Ingrese el valor 'Y' del borde superior izquierdo: "))
    #     Xid=int(input("Ingrese el valor 'X' del borde inferior derecho: "))
    #     Yid=int(input("Ingrese el valor 'Y' del borde inferior derecho: "))
    #     ventanaInicio=Ventana(t,X,Y,Xsi,Ysi,Xid,Yid)
    #     print("")
    #     print("Valores Ingreados: ")
    #     ventanaInicio.mostrar()

    print('Ventana: {} Alto: {} Ancho: {}'.format(ventanaInicio.getTitulo(),ventanaInicio.alto(),ventanaInicio.ancho()))

    print('==== Ventana Cargar ====')

    ventanaCargar= Ventana('Cargar',10,20)

    ventanaCargar.mostrar()

    print('*** Mueve a la derecha ***')

    ventanaCargar.moverDerecha(10)

    ventanaCargar.mostrar()

    print('*** Mueve a la izquierda ***')

    ventanaCargar.moverIzquierda(10)

    ventanaCargar.mostrar()

    print('*** Bajar ***')

    ventanaCargar.bajar(10)

    ventanaCargar.mostrar()

    print('==== Ventana Borrar ====')

    ventanaBorrar = Ventana('Borrar', 10,20,100,200)

    ventanaBorrar.mostrar()

    print('*** Subir ***')

    ventanaBorrar.subir()   

    ventanaBorrar.mostrar()

    print('*** Bajar ***')

    ventanaBorrar.bajar()

    ventanaBorrar.mostrar()



