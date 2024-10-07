# Inicialización del arreglo
arreglo = []

while True:
    print("\n--- Menú ---")
    print("1. Ver elementos")
    print("2. Agregar elemento")
    print("3. Modificar elemento")
    print("4. Eliminar elemento")
    print("5. Salir")
    
    opcion = input("Seleccionar opción: ")
    
    if opcion == '1':  # Ver elementos
        print("Arreglo actual:", arreglo)
    
    elif opcion == '2':  # Agregar elemento
        print("1. Mostrar arreglo actual")
        print("2. Insertar elemento")
        print("3. Mostrar nuevo arreglo con elemento")
        print("4. Preguntar si desea agregar otro o regresar al menú")
        
        sub_opcion = input("Selecciona una sub-opción: ")
        
        if sub_opcion == '1':
            print("Arreglo actual:", arreglo)
        elif sub_opcion == '2':
            nuevo_elemento = input("Introduce el nuevo elemento: ")
            arreglo.append(nuevo_elemento)
        elif sub_opcion == '3':
            print("Nuevo arreglo:", arreglo)
        elif sub_opcion == '4':
            while True:
                agregar_otro = input("¿Deseas agregar otro elemento? (s/n): ").lower()
                if agregar_otro == 's':
                    nuevo_elemento = input("Introduce el nuevo elemento: ")
                    arreglo.append(nuevo_elemento)
                    print("Nuevo arreglo:", arreglo)
                elif agregar_otro == 'n':
                    break
                else:
                    print("Opción no válida.")
        else:
            print("Sub-opción no válida.")
    
    elif opcion == '3':  # Modificar elemento
        print("Arreglo actual:", arreglo)
        indice = int(input("Introduce el índice del elemento a modificar: "))
        if 0 <= indice < len(arreglo):
            nuevo_valor = input("Introduce el nuevo valor: ")
            arreglo[indice] = nuevo_valor
            print("Elemento modificado:", arreglo)
        else:
            print("Índice fuera de rango.")
    
    elif opcion == '4':  # Eliminar elemento
        print("Arreglo actual:", arreglo)
        indice = int(input("Introduce el índice del elemento a eliminar: "))
        if 0 <= indice < len(arreglo):
            arreglo.pop(indice)
            print("Elemento eliminado. Arreglo actualizado:", arreglo)
        else:
            print("Índice fuera de rango.")
    
    elif opcion == '5':  # Salir
        print("Saliendo...")
        break
    
    else:
        print("Error: Opción no válida.")
        


