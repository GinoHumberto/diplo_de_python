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

# class Libro:

#     def __init__(self, autor, titulo):
#         self._autor = autor
#         self._titulo = titulo
#         self._disponibilidad = True
    
#     @property
#     def compartido(self):
#         return self._autor, self._titulo

#     @property
#     def disponible(self):
#         return self._disponibilidad

# class Biblioteca:

#     def __init__(self):
#         self._libros = []
    
#     def agregar_libro(self):
#         autor = input('Ingresa el nombre del autor: ')
#         titulo = input('Ingresa el título: ')
#         nuevo_libro = Libro(autor, titulo)
#         self._libros.append(nuevo_libro)
#         print(' -> Libro añadido correctamente <- \n')
    
#     def mostrar_disponibles(self):
#         print('Libros disponibles: ')
#         for libro in self._libros:
#             if libro.disponible == True:
#                 autor, titulo = libro.compartido
#                 print(autor,titulo)
#         print('<><><><><><><><><><><><><><><><><><><><><>')

#     def cambiar_disponibilidad(self, tof):
#         por_titulo = input('Ingresa el titulo del libro: ')
#         por_autor = input('Ingresa el autor del libro: ')
#         for libro in self._libros:
#             autor, titulo = libro.compartido
#             if por_autor == autor and por_titulo == titulo:
#                 libro._disponibilidad = tof
#                 return 0
#         return 1
    
#     def prestar_libro(self):
#         pedir = self.cambiar_disponibilidad(False)
#         if pedir == 0:
#             print('Retira el libro cuando gustes')
#         elif pedir == 1:
#             print('El libro no esta disponible o ingresaste mal el nombre o titulo')

#     def devolver_libro(self):
#         devolver = self.cambiar_disponibilidad(True)
#         if devolver == 0:
#             print('El libro fue devuelto con exito')
#         elif devolver == 1:
#             print('Hubo algun problema en el ingreso, revisa estar insertando bien los datos')


# lib = Biblioteca()
# def menu(num):
#     print(
#         'selecciona tu opcion \n'
#         '1. Agregar un libro \n'
#         '2. Mostrar libros disponibles \n'
#         '3. Dar un libro (prestar) \n'
#         '4. Registrar devolución del libro \n'
#         '5. Salir del programa \n'
#     )
# choice = 0
# while choice != 5:
#     menu(choice)
#     print('<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>')
#     choice = int(input('¿Que opcion seleccionaste? \n'))
#     if choice == 1:
#         lib.agregar_libro()
#     elif choice == 2:
#         lib.mostrar_disponibles()
#     elif choice == 3:
#         lib.prestar_libro()
#     elif choice == 4:
#         lib.devolver_libro()




# # # # ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ # # # #


# Crea una clase Producto con atributos nombre, precio y stock.
# Crea otra clase Tienda que maneje una lista de productos y permita:
#     Agregar productos.
#     Vender productos (disminuyendo stock).
#     Calcular el valor total del inventario.

# class Producto:

#     def __init__(self, nombre, precio, stock):
#         self._nombre = nombre
#         self._precio = precio
#         self._stock = stock

#     @property
#     def nom_producto(self):
#         return self._nombre
    
#     @property
#     def precio(self):
#         return self._precio * self._stock
    
#     @property
#     def stock(self):
#         return self._stock

#     def modificar_stock(self):
#         reducir_stock = int(input('Ingresa cuantas unidades vendiste: '))
#         self._stock = self._stock - reducir_stock
#         print(self._stock)

# class Tienda:

#     def __init__(self):
#         self._productos = []

#     def agregar_productos(self):
#         nombre = input('Ingresa el nombre del producto: ')
#         precio = float(input('Ingresa el precio unitario del producto: '))
#         stock = int(input('Ingresa la cantidad de ese producto añadido: '))
#         nuevo_producto = Producto(nombre, precio, stock)
#         self._productos.append(nuevo_producto)
#         print('El producto fue agregado con exito')
    
#     def vender_producto(self):
#         for producto in self._productos:
#             vendido = input('Qué producto vendiste? ')
#             if vendido == producto.nom_producto:
#                 producto.modificar_stock()
#             else: 
#                 print('Fijate si el producto esta registrado')
    
#     def valor_total(self):
#         total = 0
#         for producto in self._productos:
#             precios = producto.precio + total
#             total = precios
#         print(total)

#     def mostrar_inventario(self):
#         for producto in self._productos:
#             print(f'Producto: {producto.nom_producto}\n Valor total: {producto.precio}\n Stock: {producto.stock} \n <<<<<<<>>>>>>>')


# tienda = Tienda()
# def menu():
#     print(
#         'Ingresa la opción: \n'
#         '1. Agregar un producto\n'
#         '2. Vender producto\n'
#         '3. Mostrar valor del inventario\n'
#         '4. Mostrar inventario\n'
#         '5. Finalizar\n'
#     )

# choice = 0
# while choice != 5:
#     menu()
#     print('')
#     choice = int(input('Ingresa la opcion: '))
#     if choice == 1:
#         tienda.agregar_productos()
#     elif choice == 2:
#         tienda.vender_producto()
#     elif choice == 3:
#         tienda.valor_total()
#     elif choice == 4:
#         tienda.mostrar_inventario()


# # # # ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ # # # #


# Crea tres clases:
#     Plato (nombre, precio)
#     Pedido (lista de platos)
#     Mesa (número, pedido actual)
# La clase Restaurante deberá contener varias mesas y poder:
#     Tomar pedidos (agregar platos a una mesa).
#     Calcular el total de una mesa.
#     Mostrar la recaudación total del restaurante.

class Plato:
    
    def __init__(self, nombre):
        self._nombre = nombre
        self._precio = float(input('Ingresa el precio del plato: '))

    @property
    def nombre_plato(self):
        return self._nombre

    @property
    def precio(self):
        return self._precio

class Carta:

    def __init__(self):
        self._platos = []

    def agregar_plato(self):
        nuevo_plato = Plato(input('Ingresa el nombre del plato: '))
        self._platos.append(nuevo_plato)

    def quitar_plato(self):
        a_quitar = input('Ingresa el nombre del plato a quitar: ')
        for plato in self._platos:
            if plato.nombre_plato == a_quitar:
                self._platos.pop(plato)
                print('El plato fue quitado con exito')

    def ver_carta(self):
        for plato in self._platos:
            print(f'Plato: {plato.nombre_plato}\n')

    @property
    def platos(self):
        return self._platos

class Mesa:

    def __init__(self):
        self._pedidos = []
        self._cuenta = 0
        self._personas = int(input('¿De cuantas personas es la mesa? '))

    def hacer_pedido(self, carta):
        pedidos = 0
        while pedidos != self._personas:
            pedido = input('Que plato pidio? ')
            for plato in carta.platos:
                if pedido == plato.nombre_plato:
                    print('El pedido fue exitoso')
                    self._pedidos.append(pedido)
                    self._cuenta += plato.precio
                    pedidos += 1
                else: 
                    print('Algo salio mal, intenta de nuevo')
        print(f'El costo va a ser de {self._cuenta} y los platos pedidos son: {self._pedidos}')

    @property
    def cuenta(self):
        return self._cuenta
    
plato = Carta()
plato.agregar_plato()
plato.agregar_plato()
plato.ver_carta()

mesa1 = Mesa()
mesa1.hacer_pedido(plato)