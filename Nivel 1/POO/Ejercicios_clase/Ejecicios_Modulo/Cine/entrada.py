from database import Database

class NoSeEncuentraDisponible(Exception):
    def __init__(self):
        super().__init__()
        self.msg = 'No existe esa pelicula'

class Entrada():
    
    def __init__(self):
        self.__pelicula = None

    def dar_entrada(self, pelicula, peliculas_disponibles):
        pelicula_elegida = pelicula
        for fila in peliculas_disponibles:
            if pelicula_elegida == fila[0]:
                return pelicula_elegida
        raise NoSeEncuentraDisponible

