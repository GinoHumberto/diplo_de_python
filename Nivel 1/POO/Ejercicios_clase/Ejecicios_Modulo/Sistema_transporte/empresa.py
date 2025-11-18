from colectivo import Colectivos

class NoHayColectivoLibreError(Exception):
    def __init__(self):
        super().__init__()
        self.msg = 'No hay colectivos disponibles'

class Empresa:

    def __init__(self, nombre, cantidad_colectivos, destinos:dict):
        self.__nombre = nombre 
        self.__colectivos = [Colectivos(i+1) for i in range(cantidad_colectivos)]
        self.__destinos = destinos

    def asignar_destino_a_colectivo(self,colectivo,destino):
        # si metemos validaciones como verificar que el destino este en 
        # self.__destinos y que el colectivo sea de mi empresa, este 
        # método tiene bastante sentido, pero, como suponemos que los
        # valores vienen validos (solo para no complicar las cosas)
        # no tiene casi sentido hacer todo el método para asginar el destino
        # traquilamente esto se puede hacer el en main tal y como está acá
        colectivo.asignar_destino(destino)
        # Todo esto lo mandamos a obtener colectivo
        # for colectivo in self.__colectivos:
        #     if colectivo.destino_colectivo == None:
        #         colectivo.asignar_destino(destino)
        #         return True # Este return lo sacamos ya que asignar un destino
        #                     # no tiene que devolver nada, solo asignar el destino
        # return False # Si el destino no se peude asignar, entonces, en vez de devolver
        #              # false, lanzamos una excepcion (que ya se lanza en colectivo)
        #              # De hecho, esta linea nunca ocurre

    def obtener_colectivo_libre(self):
        for colectivo in self.__colectivos:
            if colectivo.destino == None:
                return colectivo
        raise NoHayColectivoLibreError

    def generar_boleto(self, destino):
        for colectivo in self.__colectivos:
            if destino == colectivo.destino:
                asiento = colectivo.disponibilidad_asientos()
                if asiento:
                    asiento.asignar_pasajero()
                    return colectivo, asiento
        raise NoHayColectivoLibreError  
