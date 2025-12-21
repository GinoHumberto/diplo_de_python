from empresa import Empresa
from salas import Sala
from database import Database

class NoSeEncuentraDisponible(Exception):
    def __init__(self):
        super().__init__()
        self.msg = 'No hay disponibilidad de salas con esa película'

class Entrada:
    
    def __init__(self, precio):
        self.__precio = precio
        self.__pelicula = None
        self.__sala = None
        self.__asiento = None

    def vender_entrada(self, pelicula):
        Empresa().ingresos(self.__precio)
        sala_id, peliculas_disponibles = Database().devolver_sala(pelicula)
        if peliculas_disponibles:
            self.__pelicula = peliculas_disponibles
            self.__sala = sala_id
            self.__asiento = Sala().asignar_asiento()
            Database().registrar_venta(pelicula)
            return self.__asiento, self.__sala, self.__pelicula
        raise NoSeEncuentraDisponible

    
        
       