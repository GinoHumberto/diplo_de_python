from database import Database
from entrada import Entrada
from empresa import Empresa

db = Database()
entrada = Entrada()
empresa = Empresa()
# ---- CREO EMPRESA CON 10 ASIENTOS POR SALA ----#
empresa(10)

# CODIGO IA PARA CARGAR DATOS DE SQLITE:
peliculas_guardadas = db.obtener_todas_las_peliculas()
empresa.cargar_peliculas_desde_db(peliculas_guardadas)
#----------- Mi codigo ------------#

def asignar_tipo_a_salas(tipo):
    empresa.pasar_tipo_a_sala(tipo)

def nombre_y_genero():
    pelicula = input('Ingresa el nombre de la película: ')
    genero = input('Ingresa el género de la pelicula: ')
    return pelicula, genero

def nombre_pelicula():
    pelicula_vieja = input('Ingresa el nombre de la película: ')
    return pelicula_vieja

# <><><><><><><><><><> #
#        MENUS         #
# <><><><><><><><><><> #

def menu_general():
    print(
        '\nBienvenido al Menu, selecciona la opción:\n'
        '0. Salir del menu \n'
        '1. Gestionar salas \n'
        '2. Gestionar entradas e inventario \n'
    )

def menu_salas():
    print(
        '\nBienvenido al Menu de salas, selecciona la opción:\n'
        '0. Volver al menu principal \n'
        '1. Agregar pelicula \n'
        '2. Cambiar pelicula \n'
        '3. Mostrar peliculas disponibles\n'
    )

def menu_entradas():
    print(
        '\nBienvenido al Menu de entradas, selecciona la opción:\n'
        '0. Volver al menu principal \n'
        '1. Dar una entrada \n'
    )

#################################
#        GESTOR GENERAL         #
#################################

def gestor_general():
    choice = 1 
    while choice != 0:
        print(menu_general())
        choice = int(input('Seleciona la opción que desea: '))
        if choice == 0:
            db.cerrar_conexion()
        if choice == 1:
            gestor_salas()
        if choice == 2:
            gestor_entradas()

##################################
#        GESTOR DE SALAS         #
##################################

def gestor_salas():
    choice = 1
    while choice != 0:
        print(menu_salas())
        choice = int(input('Seleciona la opción que desea: '))
        
        if choice == 0:
            gestor_general()

        elif choice == 1:  # AGREGA UNA PELICULA
            pelicula, genero = nombre_y_genero()
            if empresa.asignar_pelicula_sala(pelicula) == True:
                db.agregar_pelicula(pelicula, genero)
        
        elif choice == 2:  # CAMBIA UNA PELICULA YA ASIGNADA
            print('Pelicula nueva')
            nombre, genero = nombre_y_genero()
            print('Pelicula a remplazar')
            pelicula_vieja = nombre_pelicula()
            if empresa.cambiar_pelicula_sala(pelicula_vieja, nombre) == True:
                db.cambiar_pelicula(pelicula_vieja, nombre, genero)

        elif choice == 3:  # MUESTRA LAS PELICULAS DISPONIBLES
            peliculas_disponibles = db.mostrar_peliculas_disponibles()
            for fila in peliculas_disponibles:
                print(fila[0])

##################################
#        GESTOR ENTRADAS         #
##################################

def gestor_entradas():
    choice = 1
    while choice != 0:
        print(menu_entradas())
        choice = int(input('Seleciona la opción que desea: '))
        
        if choice == 0:
            gestor_general()

        elif choice == 1:  # OTORGA UNA ENTRADA
            pelicula_seleccionada = entrada.dar_entrada(nombre_pelicula(), db.mostrar_peliculas_disponibles())
            if empresa.asignar_asiento_sala(pelicula_seleccionada) == True:
                db.registrar_venta(pelicula_seleccionada)


# <><><><><><><><><><> #
#      EJECUCION       #
# <><><><><><><><><><> #

salas = {'sala_1' : '2D', 'sala_2' : '2D', 'sala_3' : '3D', 'sala_4' : '3D'}

for sala in salas:
    asignar_tipo_a_salas(sala)
gestor_general()