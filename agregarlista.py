# lista.py

# Inicializamos la lista
mi_lista = []

def mostrar_lista():
    print("Elementos en la lista:")
    for item in mi_lista:
        print(f"- {item}")

def agregar_elemento(elemento):
    mi_lista.append(elemento)
    print(f"'{elemento}' agregado a la lista.")

def main():
    while True:
        print("\n1. Agregar elemento")
        print("2. Mostrar lista")
        print("3. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            elemento = input("Ingrese el elemento a agregar: ")
            agregar_elemento(elemento)
        elif opcion == '2':
            mostrar_lista()
        elif opcion == '3':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()


