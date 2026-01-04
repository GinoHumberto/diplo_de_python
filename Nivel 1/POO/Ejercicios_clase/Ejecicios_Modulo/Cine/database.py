import sqlite3

class Database:

    def __init__(self):
        self.conexion = sqlite3.connect('Bichopolis.db')
        self.cursor = self.conexion.cursor()
        self.cursor.execute("PRAGMA foreign_keys = ON")
        
        # CREACION DE TABLAS
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

    def registrar_venta(self, pelicula):
        self.cursor.execute(
            'INSERT INTO ventas (pelicula) VALUES (?)', (pelicula,)
        )
        self.conexion.commit()

    def cerrar_conexion(self):
        self.conexion.close()
    

# Dado como idea por la IA: (objetivo que empresa no este vacio cuando lo vuelva a ejecutar)
    def obtener_todas_las_peliculas(self):
        self.cursor.execute(
            'SELECT pelicula, genero FROM peliculas'
        )
        return self.cursor.fetchall()
# Sigue en empresa