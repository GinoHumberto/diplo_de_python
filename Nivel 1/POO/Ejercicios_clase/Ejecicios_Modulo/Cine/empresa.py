from salas import Sala
from entrada import Entrada
from database import Database

class NoHaySalaDisponible(Exception):
    def __init__(self):
        super().__init__()
        self.msg = 'No Hay salas disponibles'

class Empresa:

    def __init__(self):
        self.__cantidad_salas = [Sala(i+1) for i in range(4)]
        self.__cantidad_peliculas = 4

    def ingresos(self, precio):
        ingresos = 0
        ingresos += precio
        return ingresos

    def nueva_pelicula(self, nombre, genero):
        Database().agregar_pelicula(nombre, genero)

    
    

    