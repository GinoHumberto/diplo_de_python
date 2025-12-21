
class Asiento:

    def __init__(self):
        self.__libre = True
    
    def ocupar_asiento(self):
        self.__libre = False
        