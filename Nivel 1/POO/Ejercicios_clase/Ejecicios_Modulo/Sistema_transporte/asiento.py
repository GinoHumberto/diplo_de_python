class Asiento:

    def __init__(self,id):
        self.__id = id
        self.__pasajero = None

    @property
    def numero(self):
        return self.__id

    def libre(self):
        if self.__pasajero == None:
            return True
        return False

    def asignar_pasajero(self):
        self.__pasajero = 'Ocupado'