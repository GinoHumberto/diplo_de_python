# Plantear un programa que permita jugar a los dados. Las reglas de juego son:
# se tiran tres dados si los tres salen con el mismo valor mostrar un mensaje que "gano", sino
# "perdió".
from random import randint

class Persona:

    def tirar_dado():
        valor = random.randint(1,6)

class Dado:

    def __init__(self):
        self._valor = Persona.tirar_dado()
    
    @property
    def numero(self):
        return self._valor
    
    def mostrar(numero):
        print(numero)

class JuegoDeDado:

    def __init__(self):
        self._dado1 = Dado()
        self._dado2 = Dado()
        self._dado3 = Dado()

    def juego():
        dado1 = self.dado1.numero
        dado2 = self.dado2.numero
        dado3 = self.dado3.numero
        self.dado1.mostrar()
        self.dado2.mostrar()
        self.dado3.mostrar()
        if dado1 == dado2 and dado1 == dado3:

            print('ganaste')
        else:
            print('Perdiste')

jugar = JuegoDeDado()
juego.jugar()