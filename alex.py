# Programa para clasificar a una persona según su edad

edad = int(input("Ingresa la edad de la persona: "))

if edad >= 0 and edad <= 2:
    print("Es un bebé.")
elif edad > 2 and edad <= 12:
    print("Es un niño.")
elif edad > 12 and edad <= 18:
    print("Es un adolescente.")
elif edad > 18 and edad <= 59:
    print("Es un adulto.")
elif edad >= 60:
    print("Es un adulto mayor.")
else:
    print("Edad no válida.")