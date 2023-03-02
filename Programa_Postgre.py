from Funciones_Posgre import *

db = conectarBD("localhost","josema","josema","proyecto")
opcion = menu()
while opcion != 0:
    if opcion == 1:
        listarAminales(db)
    if opcion == 2:
        clinica(db)
    if opcion == 3:
        animalesPropietario(db)
    if opcion == 4:
        animal = {}
        animal["codigo"] = int(input("codigo: "))
        animal["nombre"] = input("Nombre: ")
        animal["especie"] = input("Especie: ")
        animal["raza"] = input("Raza: ")
        animal["color_pelo"] = input("Color de pelo: ")
        animal["fecha_nacimiento"] = input("Fecha de nacimiento: ")
        animal["DNI_propietario"] = input("Dni del propietario: ")
        insertarAnimal(db,animal)
    if opcion == 5:
        nombre = input("Introduce el nombre del animal a borrar: ")
        eliminarAnimal(db,nombre)
    if opcion == 6:
        nombre = input("Introduce el nombre de la clinica ")
        direccion = input("Introduce la nueva direccion ")
        actualizarClinica(db, nombre,direccion)
        
    opcion=menu()