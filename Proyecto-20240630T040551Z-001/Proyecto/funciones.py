def escoger_Opcion(lista):
    for index, elemento in enumerate(lista):
        print(f"Opcion {index +1} \n{elemento}")
        print()
        
    while True:
        try:
            ingrese_numero = int(input("Ingrese el número de la opción que desea elegir: "))
            
            if ingrese_numero <= 0:
                raise Exception

            eleccion = lista[ingrese_numero - 1]
            return eleccion
        except:
            print("Ingrese una opción válida")
def escoger_Estadio(lista):
    for index, elemento in enumerate(lista):
        print(f"Opcion {index +1} \n{elemento.name}")
        print()
        
    while True:
        try:
            ingrese_numero = int(input("Ingrese el número de la opción que desea elegir: "))
            
            if ingrese_numero <= 0:
                raise Exception

            eleccion = lista[ingrese_numero - 1]
            return eleccion
        except:
            print("Ingrese una opción válida")

