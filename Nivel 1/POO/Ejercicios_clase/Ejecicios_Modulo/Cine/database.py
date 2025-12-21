import sqlite3

class Database:

    def __init__(self):
        self.__conexion = sqlite3.connect('Bichopolis.db')
        self.__cursor = self.__conexion.cursor()
        self.__cursor.execute("PRAGMA foreign_keys = ON")

        self.__tabla_peliculas = self.__cursor.execute(
            '''CREATE TABLE IF NOT EXISTS peliculas (
            sala_id INTEGER PRIMARY KEY AUTOINCREMENT, 
            pelicula TEXT UNIQUE, genero TEXT)'''
        )
        self.__tabla_ventas = self.__cursor.execute(
            '''CREATE TABLE IF NOT EXISTS ventas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pelicula TEXT, fecha TEXT DEFAULT CURRENT_TIMESTAMP, 
            FOREIGN KEY (pelicula) REFERENCES peliculas(pelicula))'''
        )
        
    def agregar_pelicula(self, nombre, genero):
        self.__cursor.execute(
            '''INSERT INTO peliculas (pelicula, genero) VALUES (?, ?)''', (nombre, genero)
        )
        self.__conexion.commit()
    
    def registrar_venta(self, nombre):
        self.__cursor.execute(
            '''INSERT INTO ventas (pelicula) VALUES (?)''', (nombre, )
        )
        self.__conexion.commit()

    @property
    def devolver_sala(self, pelicula):
        self.__cursor.execute(
            'SELECT sala_id, pelicula FROM peliculas WHERE pelicula = ?' (pelicula, )
        )
        if self.__cursor.fetchone():
            return self.__cursor.fetchone()[0]
        else:
            return None