# Plantear un programa que permita jugar a los dados. Las reglas de juego son:
# se tiran tres dados si los tres salen con el mismo valor mostrar un mensaje que "gano", sino
# "perdió".

# from random import randint

# class Dado:

#     def __init__(self):
#         self._valor = None

#     def tirar(self):
#         self._valor = randint(1,6)
    
#     @property
#     def valor(self):
#         return self._valor
    
# class JuegoDado:

#     def __init__(self):
#         self._bolsa_dados = [Dado() for _ in range(3)]
#         self._valor_en_mesa = []

#     def jugar(self):
#         for dado in self._bolsa_dados:
#             dado.tirar()
#             self._valor_en_mesa.append(dado.valor)
#         previo = self._valor_en_mesa[0]
#         for i in range(1, 3):
#             if previo == self._valor_en_mesa[i]:
#                 previo = self._valor_en_mesa[i]
#             else:
#                 return 'Perdiste'
#         return 'Ganaste'

#     def ver_valores(self):
#         return self._valor_en_mesa

# juego = JuegoDado()
# resultado = juego.jugar()
# print(juego.ver_valores())
# print(resultado)

# # # # ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ # # # #

# Crea una clase Libro que tenga atributos como título, autor y si está disponible o no.
# Luego crea una clase Biblioteca que contenga una lista de libros y tenga métodos como:
# - agregar_libro(libro)
# - prestar_libro(titulo)
# - devolver_libro(titulo)
# - mostrar_disponibles()

class Libro:

    def __init__(self, autor, titulo):
        self._autor = autor
        self._titulo = titulo
        self._disponibilidad = True
    
    @property
    def compartido(self):
        return self._autor, self._titulo

class Biblioteca:

    def __init__(self):
        self._libros = []
    
    def agregar_libro(self):
        autor = input('Ingresa el nombre del autor: ')
        titulo = input('Ingresa el título: ')
        Libro(autor, titulo)
        self._libros.append(Libro)
    
    def mostrar_disponibles(self):
        for n in range(len(self._libros)):
            libro = self._libros[n]
            if libro._disponibilidad == True:
                return Libro.compartido
    

lib = Biblioteca()
lib.agregar_libro()
lib.mostrar_disponibles()