from salas import Sala

# <><><><><><><><><><> #
#       ERRORES        #
# <><><><><><><><><><> #

class NoHaySalaConEsaPelicula(Exception):
    def __init__(self):
        super().__init__()
        self.msg = 'No Hay sala con esa pelicula'

class NoHaySalaDisponible(Exception):
    def __init__(self):
        super().__init__()
        self.msg = 'No Hay salas libres'

# <><><><><><><><><><> #
#       EMPRESA        #
# <><><><><><><><><><> #

class Empresa:

    def __init__(self):
        self.__cantidad_salas = [Sala() for i in range(4)]

    def asignar_asiento_sala(self, pelicula_seleccionada):
        for sala in self.__cantidad_salas:
            if sala.pelicula_asignada == pelicula_seleccionada:
                if sala.asignar_asiento() == True:
                    return True

    def asignar_pelicula_sala(self, pelicula, tipo):
        for sala in self.__cantidad_salas:
            if sala.pelicula_asignada == None:
                sala.asignar_pelicula(pelicula)
                return True
        raise NoHaySalaDisponible

    def cambiar_pelicula_sala(self, pelicula_vieja, pelicula):
        for sala in self.__cantidad_salas:
            if sala.pelicula_asignada == pelicula_vieja:
                sala.asignar_pelicula(pelicula)
                return True
        raise NoHaySalaConEsaPelicula





# Dado como idea por la IA:
    def cargar_peliculas_desde_db(self, lista_peliculas):
        for i, datos in enumerate(lista_peliculas):
            if i < len(self.__cantidad_salas):
                pelicula = datos[0]
                # Asignamos la película a la sala correspondiente
                self.__cantidad_salas[i].asignar_pelicula(pelicula)

# enumerate() toma la lista y la convierte en una lista de parejas.Es decir da la pelicula y el genero
# i es la sala
# datos son los elementos de la base de datos

    