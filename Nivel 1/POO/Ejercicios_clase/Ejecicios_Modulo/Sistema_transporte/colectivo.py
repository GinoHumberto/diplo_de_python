from asiento import Asiento

class DestinoYaAsignadoError(Exception):
    def __init__(self):
        super().__init__()
        self.msg = 'El colectivo ya tiene un destino asignado'

class Colectivos:

    def __init__(self,id):
        self.__id = id
        self.__asientos = [Asiento(i+1) for i in range(4)]
        self.__destino = None

    @property
    def numero(self):
        return self.__id

    @property
    def destino(self):
        if self.__destino == None:
            return None
        else:
            return self.__destino

    def asignar_destino(self, destino):
        if self.__destino == None:
            self.__destino = destino
        else:
            raise DestinoYaAsignadoError

    def disponibilidad_asientos(self): # obtener asiento libre
        for asiento in self.__asientos:
            if asiento.libre():
                return asiento
