import sqlite3

class Database:

    def __init__(self):
        self.conexion = sqlite3.connect('Bichopolis.db')
        self.cursor = self.conexion.cursor()
        self.cursor.execute("PRAGMA foreign_keys = ON")
        
        # <><><><><><><><><><> #
        #  CREACION DE TABLAS  #
        # <><><><><><><><><><> #

        tabla_peliculas = self.cursor.execute(
            '''CREATE TABLE IF NOT EXISTS peliculas (
            sala_id INTEGER PRIMARY KEY AUTOINCREMENT, 
            pelicula TEXT UNIQUE, genero TEXT)'''
        )

        tabla_ventas = self.cursor.execute(
            '''CREATE TABLE IF NOT EXISTS ventas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pelicula TEXT, fecha TEXT DEFAULT CURRENT_TIMESTAMP, 
            FOREIGN KEY (pelicula) REFERENCES peliculas(pelicula))'''
        )

        tabla_salas = self.cursor.execute(
            '''CREATE TABLE IF NOT EXISTS salas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tipo TEXT, pelicula TEXT, FOREIGN KEY (pelicula)
            REFERENCES peliculas (pelicula))'''
        )

    # <><><><><><><><><><><><><><><><><> #
    #  FUNCIONES DE LA TABLA PELICULAS   #
    # <><><><><><><><><><><><><><><><><> #
        
    def agregar_pelicula(self, pelicula, genero):
        self.cursor.execute(
            'INSERT INTO peliculas (pelicula, genero) VALUES (?, ?)', (pelicula, genero)
            )
        
        self.conexion.commit()

    def cambiar_pelicula(self, pelicula_vieja, pelicula, genero):
        self.cursor.execute(
            '''UPDATE peliculas
            SET pelicula = (?), genero = (?)
            WHERE pelicula = ?''', (pelicula, genero, pelicula_vieja)
        )
        self.conexion.commit()

    def mostrar_peliculas_disponibles(self):
        peliculas_disponibles = self.cursor.execute(
            'SELECT pelicula FROM peliculas'
        )
        return peliculas_disponibles

    # <><><><><><><><><><><><><><><><> #
    #   FUNCIONES DE LA TABLA VENTAS   #
    # <><><><><><><><><><><><><><><><> #

    def registrar_venta(self, pelicula):
        self.cursor.execute(
            'INSERT INTO ventas (pelicula) VALUES (?)', (pelicula,)
        )
        self.conexion.commit()

    # <><><><><><><><><><><><><><><> #
    #  FUNCIONES DE LA TABLA SALAS   #
    # <><><><><><><><><><><><><><><> #

    def asignar_pelicula_a_sala(self, pelicula, tipo):
        self.cursor.execute(
            'INSERT INTO salas (tipo, pelicula) VALUES (?, ?)', (tipo, pelicula)
        )
        self.conexion.commit


    # <><><><><><><><><> #
    #   OTRAS FUNCIONES  #
    # <><><><><><><><><> #

    def cerrar_conexion(self):
        self.conexion.close()


# Dado como idea por la IA: (objetivo que empresa no este vacio cuando lo vuelva a ejecutar)

    def obtener_todas_las_peliculas(self):
        self.cursor.execute(
            'SELECT pelicula, genero FROM peliculas'
        )
        return self.cursor.fetchall()

# Sigue en empresa