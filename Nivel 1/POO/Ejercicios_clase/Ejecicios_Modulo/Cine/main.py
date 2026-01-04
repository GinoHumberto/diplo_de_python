from database import Database
from entrada import Entrada
from empresa import Empresa

db = Database()
entrada = Entrada()
empresa = Empresa()

# CODIGO IA PARA CARGAR DATOS DE SQLITE:
peliculas_guardadas = db.obtener_todas_las_peliculas()
empresa.cargar_peliculas_desde_db(peliculas_guardadas)
#----------- Mi codigo ------------#

def menu():
    print(
        '\nBienvenido al Menu, selecciona la opción:\n'
        '0. Salir del menu \n'
        '1. Agregar pelicula \n'
        '2. Cambiar pelicula \n'
        '3. Dar entrada\n'
        '4. Mostrar peliculas disponibles'
    )

def nombre_y_genero():
    pelicula = input('Ingresa el nombre de la película: ')
    genero = input('Ingresa el género de la pelicula: ')
    return pelicula, genero

def nombre_pelicula():
    pelicula_vieja = input('Ingresa el nombre de la película: ')
    return pelicula_vieja

choice = 1
while choice != 0:
    print(menu())
    choice = int(input('Seleciona la opción que desea: '))
    if choice == 0:
        db.cerrar_conexion()
    if choice == 1:
        pelicula, genero = nombre_y_genero()
        if empresa.asignar_pelicula_sala(pelicula) == True:
            db.agregar_pelicula(pelicula, genero)
    elif choice == 2:
        print('Pelicula nueva')
        nombre, genero = nombre_y_genero()
        print('Pelicula a remplazar')
        pelicula_vieja = nombre_pelicula()
        if empresa.cambiar_pelicula_sala(pelicula_vieja, nombre) == True:
            db.cambiar_pelicula(pelicula_vieja, nombre, genero)
    elif choice == 3:
        pelicula_seleccionada = entrada.dar_entrada(nombre_pelicula(), db.mostrar_peliculas_disponibles())
        if empresa.asignar_asiento_sala(pelicula_seleccionada) == True:
            db.registrar_venta(pelicula_seleccionada)
    elif choice == 4:
        peliculas_disponibles = db.mostrar_peliculas_disponibles()
        for fila in peliculas_disponibles:
            print(fila[0])