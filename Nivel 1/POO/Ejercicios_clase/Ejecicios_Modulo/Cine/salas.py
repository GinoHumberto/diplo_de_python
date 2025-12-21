from asientos import Asiento
from database import Database

class NoHayAsientos(Exception):
    def __init__(self):
        super().__init__()
        self.msg = 'No Hay asientos disponibles'

class Sala:

    def __init__(self):
        sala_id, pelicula = Database().devolver_sala
        self.__numero_sala = sala_id
        self.__asientos = [Asiento(i+1) for i in range(10)]
        self.__pelicula_asignada = pelicula

    def asignar_asiento(self):
        for asiento in range(self.__asientos):
            if asiento == True:
                Asiento().ocupar_asiento()
        raise NoHayAsientos

    @property
    def pelicula_asignada(self):
        return self.__pelicula_asignada

    @property
    def numero_de_sala(self):
        return self.__numero_sala