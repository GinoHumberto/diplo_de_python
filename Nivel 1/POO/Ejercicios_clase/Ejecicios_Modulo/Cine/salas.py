from asientos import Asiento

# <><><><><><><><><><> #
#       ERRORES        #
# <><><><><><><><><><> #

class NoHayAsientos(Exception):
    def __init__(self):
        super().__init__()
        self.msg = 'No Hay asientos disponibles'   

# <><><><><><><><><><> #
#        SALAS         #
# <><><><><><><><><><> #

class Sala():
    
    def __init__(self):
        self.__asientos = [Asiento() for i in range(10)]
        self.__pelicula = None
        self.__tipo = None

    def asignar_asiento(self):
        for asiento in self.__asientos:
            if asiento.asiento_libre == True:
                asiento.ocupar_asiento()
                return True
        raise NoHayAsientos
     
    @property
    def pelicula_asignada(self):
        return self.__pelicula
    
    def asignar_pelicula(self, pelicula):
        self.__pelicula = pelicula